from django.db import models

class Preference(models.Model):
    user = models.OneToOneField('user_app.CustomUser', on_delete=models.CASCADE, related_name="preference")
    
    # Using JSONField to store range as dictionary for fields that require ranges
    age_range = models.JSONField(blank=True, null=True)  # Example: {"min": 20, "max": 30}
    income_range = models.JSONField(blank=True, null=True)  # Example: {"min": 50000, "max": 100000}
    height_range = models.JSONField(blank=True, null=True)  # Example: {"min": 150.5, "max": 180.5}
    weight_range = models.JSONField(blank=True, null=True)  # Example: {"min": 50.5, "max": 80.5}

    # Using JSONField to store multiple options as lists
    gender = models.CharField(max_length=10, blank=True, null=True)  # Single selection for gender

    # Fields that can have multiple options
    religion = models.JSONField(blank=True, null=True)  # Example: ["Hindu", "Muslim"]
    caste = models.JSONField(blank=True, null=True)  # Example: ["Brahmin", "Kshatriya"]
    profession = models.JSONField(blank=True, null=True)  # Example: ["Engineer", "Doctor"]
    education = models.JSONField(blank=True, null=True)  # Example: ["Bachelor's", "Master's"]
    location = models.JSONField(blank=True, null=True)  # Example: ["New York", "San Francisco"]
    language = models.JSONField(blank=True, null=True)  # Example: ["English", "Hindi"]
    marital_status = models.JSONField(blank=True, null=True)  # Example: ["Single", "Divorced"]
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Preferences"
