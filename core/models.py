from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, role=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not role:
            raise ValueError('The Role field must be set')
        
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, role='admin', **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('renter', 'Renter'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    objects = UserManager()



class TrailerRentalRequest(models.Model):
    owner_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    trailer_details = models.CharField(max_length=500)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Store the password securely
        self.password = make_password(self.password)  # Hash the password
        super().save(*args, **kwargs)