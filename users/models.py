from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model that extends the default Django user.
    """
    email = models.EmailField(unique=True)

    # Basic Information
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # Identity Documents (storing paths to encrypted files)
    selfie_path = models.CharField(max_length=255, blank=True)
    selfie_with_id_path = models.CharField(max_length=255, blank=True)
    id_card_path = models.CharField(max_length=255, blank=True)
    passport_path = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
