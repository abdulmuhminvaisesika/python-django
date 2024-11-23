from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone  # Import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(user_id=user_id, username=username, **extra_fields)
        user.set_password(password)  # Hashes password
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(user_id, username, password, **extra_fields)

class CustomUser(AbstractBaseUser):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('suspended_user', 'Suspended User'),
    ]


    user_id= models.CharField(max_length=50, unique=True, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role=models.CharField(max_length=255, choices=ROLE_CHOICES, default='user')

    subcription_plan = models.ForeignKey('subcription_app.SubcriptionTable', on_delete =models.CASCADE , null=True, blank=True)  # Missing default value
    
    join_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_id', 'first_name']

    def save(self, *args, **kwargs):

        # Adjust permissions and active status based on the role
        if self.role == 'admin':
            self.is_superuser = True
            self.is_staff = True
            self.is_active = True
            self.is_admin = True
            self.subcription_plan = None
        elif self.role == 'user':
            self.is_superuser = False
            self.is_staff = False
            self.is_active = True
            self.is_admin = False
        elif self.role == 'suspended_user':
            self.is_superuser = False
            self.is_staff = False
            self.is_active = False
            self.is_admin = False


        # Ensure password is hashed before saving
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Returns True if the user has a specific permission"""
        return True

    def has_module_perms(self, app_label):
        """Returns True if the user has permissions for a specific app"""
        return True