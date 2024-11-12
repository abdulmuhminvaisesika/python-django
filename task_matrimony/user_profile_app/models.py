from django.db import models

class User_Profile_Table(models.Model):
    # Avoid circular import by using lazy imports
    user = models.OneToOneField('user_app.CustomUser', on_delete=models.CASCADE, related_name="profile")
    
    # Use ForeignKey to link to Common_Matching table for specific types
    age = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'age'}, related_name='age_profiles')
    gender = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'gender'}, related_name='gender_profiles')
    dob = models.DateField()
    bio = models.TextField(blank=True, null=True)
    weight = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'weight'}, related_name='weight_profiles')
    height = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'height'}, related_name='height_profiles')
    religion = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'religion'}, related_name='religion_profiles')
    caste = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'caste'}, related_name='caste_profiles')
    income = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'income'}, related_name='income_profiles')
    profession = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'profession'}, related_name='profession_profiles')
    education = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'education'}, related_name='education_profiles')
    location = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'location'}, related_name='location_profiles')
    marital_status = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'marital_status'}, related_name='marital_status_profiles')
    language = models.ForeignKey('common_maching_app.Common_Matching', on_delete=models.CASCADE, limit_choices_to={'type': 'language'}, related_name='language_profiles')
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Profile"
