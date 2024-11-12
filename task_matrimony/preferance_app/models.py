from django.db import models
from django.apps import apps  # For lazy importing

class Preference(models.Model):

    user = models.OneToOneField('user_app.CustomUser', on_delete=models.CASCADE, related_name="preference")
    
    # Lazy import for Common_Matching to avoid circular import
    age = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_age', limit_choices_to={'type': 'age'})
    gender = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_gender', limit_choices_to={'type': 'gender'})
    religion = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_religion', limit_choices_to={'type': 'religion'})
    caste = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_caste', limit_choices_to={'type': 'caste'})
    income = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_income', limit_choices_to={'type': 'income'})
    profession = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_profession', limit_choices_to={'type': 'profession'})
    education = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_education', limit_choices_to={'type': 'education'})
    location = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_location', limit_choices_to={'type': 'location'})
    height = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_height', limit_choices_to={'type': 'height'})
    weight = models.ManyToManyField('common_maching_app.Common_Matching', related_name='user_preferences_weight', limit_choices_to={'type': 'weight'})
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Preferences"
