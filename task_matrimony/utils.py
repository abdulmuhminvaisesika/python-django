# utils.py
from django.apps import apps
from django.shortcuts import get_object_or_404

from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers



def validate_common_matching(field_values, field_type):
    """
    Validates each value in a list or single value against the Common_Matching table
    for the specified type.
    """
    Common_Matching = apps.get_model('common_maching_app', 'Common_Matching')
    # If the field is a single value, convert it to a list for validation
    if not isinstance(field_values, list):
        field_values = [field_values]
    
    for value in field_values:
        if not Common_Matching.objects.filter(name=value, type=field_type).exists():
            raise serializers.ValidationError(f"'{value}' is not a valid option for '{field_type}' in master table.")
    
    if len(field_values) == 1:
        return field_values[0]
    else:
        return field_values

    



def get_user_object_or_permission_denied(user_id, model_class, request_user):
    """
    Utility function to get a user profile or preference by user_id and ensure the authenticated user can only access their own profile/preference.
    
    Args:
    - user_id: The ID of the user (from the URL).
    - model_class: The model class (`User_Profile_Table` or `Preference`) to query.
    - request_user: The currently authenticated user.
    
    Returns:
    - Instance of the model class (UserProfile or Preference).
    
    Raises:
    - PermissionDenied if the user is trying to access a different user's profile.
    """
    # Get the user associated with the user_id
    user = get_object_or_404(apps.get_model('user_app', 'CustomUser'), user_id=user_id)
    
    # Get the specific profile or preference for the user
    obj = get_object_or_404(model_class, user=user)
    
    # Ensure the object belongs to the authenticated user
    if obj.user != request_user:
        raise PermissionDenied("You do not have permission to access or modify this data.")
    
    return obj



def calculate_matching_score(user1_preferences, user2_profile):
    """
    Calculate matching score based on the preferences of user1 and the profile of user2.
    High-priority fields (gender) use exact matches, while other fields use multi-option and range-based scoring.
    """
    score = 0

    # Exact Match - High Priority
    if user1_preferences.gender and user1_preferences.gender == user2_profile.gender:
        print(">>>>>>>>>>>", user1_preferences.gender)
        print(">>>>>>>>>>>", user2_profile.gender)
        score += 5
    else:
        # Early exit if gender is a must-have criterion
        return 0  # No match possible if gender criterion fails
    print(">>>>>>>>>>>gender_score", score)

    # Multi-option Fields (Moderate Priority)
    multi_option_fields = [
    ('religion', 'religion'),
    ('caste', 'caste'),
    ('profession', 'profession'),
    ('education', 'education'),
    ('location', 'location'),
    ('language', 'language'),
    ('marital_status', 'marital_status')
    ]

    for user1_field, user2_field in multi_option_fields:
        user1_value = getattr(user1_preferences, user1_field, None)
        print(f"User1 Value", user1_value)
        user2_value = getattr(user2_profile, user2_field, None)
        print(f"User2 Value", user2_value)

        if user1_value and user2_value:
            for value in user1_value:
                if value in user2_value:
                    score += 2  # Low priority for multi-option match
                    print(">>>>>>>>>>>", value)
                    print(">>>>>>>>>>>", score)
                
        
            
            


    # Range-based Fields (Age, Height, Weight, Income)
    range_fields = {
        'age_range': 'age',
        'income_range': 'income',
        'height_range': 'height',
        'weight_range': 'weight'
    }

    for preference_range_field, profile_field in range_fields.items():
        # Get the range dictionary (e.g., {'from': 25, 'to': 30})
        range_values = getattr(user1_preferences, preference_range_field, None)
        # Get the value from user2's profile (e.g., age, income)
        profile_value = getattr(user2_profile, profile_field, None)

        if range_values and profile_value is not None:
            min_value = range_values.get('from')
            print(">>>>>>>>>>>", min_value)
            max_value = range_values.get('to')
            print(">>>>>>>>>>>", max_value)
            # Check if the profile value falls within the 'from' and 'to' range
            if min_value is not None and max_value is not None and min_value <= profile_value <= max_value:
                print(">>>>>>>>>>>", profile_value)
                score += 1  # Low priority for range field match
    print(">>>>>>>>>>>range_fields_score", score)

    # Normalize the score to be out of 100
    max_score = 23  # Define the actual maximum possible score (5 + 14 + 4 = 23)
    normalized_score = (score / max_score) * 100  # Scale the score to be out of 100
    print(">>>>>>>>>>>normalized_score", normalized_score)
    return round(normalized_score, 2)
