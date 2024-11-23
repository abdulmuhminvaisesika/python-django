import ast
from user_profile_app.models import User_Profile_Table

def convert_list_to_string():
    """Convert single-item list-like strings in specified fields to plain strings."""
    fields_to_check = [
        'location', 'education', 'profession', 'caste', 'religion',
        'gender', 'marital_status', 'language'
    ]

    profiles = User_Profile_Table.objects.all()
    print(f"Found {profiles.count()} profiles to process.")

    for profile in profiles:
        profile_updated = False  # Track if the profile needs to be saved
        for field in fields_to_check:
            field_value = getattr(profile, field, None)

            print(f"Checking {field} for profile {profile.user}: {field_value}")

            if isinstance(field_value, str):
                # Check if the field is a string that looks like a list
                if field_value.startswith('[') and field_value.endswith(']'):
                    try:
                        # Safely evaluate the string to a Python list
                        parsed_list = ast.literal_eval(field_value)
                        
                        # Check if it's a list with one element
                        if isinstance(parsed_list, list) and len(parsed_list) == 1:
                            string_value = parsed_list[0]  # Extract the single value
                            setattr(profile, field, string_value)  # Update the field
                            print(f"Updated {field} for profile {profile.user} to: {string_value}")
                            profile_updated = True
                    except Exception as e:
                        print(f"Error parsing {field} for profile {profile.user}: {e}")
        
        # Save the profile only if an update was made
        if profile_updated:
            profile.save()
            print(f"Profile {profile.user} updated and saved.")

    print("Finished processing all profiles.")
    

def run():
    convert_list_to_string()