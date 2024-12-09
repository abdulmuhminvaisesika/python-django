from django.db import models
from datetime import date
from django.forms import ValidationError


class User_Profile_Table(models.Model):
    # Avoid circular import by using lazy imports
    user = models.OneToOneField('user_app.CustomUser', on_delete=models.CASCADE, related_name="profile")
    
    age = models.IntegerField(blank=True, null=True)  # Age as an integer field
    gender = models.CharField(max_length=10, blank=True, null=True)  # Gender as a character field
    dob = models.DateField()
    bio = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Weight as decimal
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Height as decimal
    religion = models.CharField(max_length=50, blank=True, null=True)
    caste = models.CharField(max_length=50, blank=True, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Income as decimal
    profession = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
