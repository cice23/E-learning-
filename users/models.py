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

    # Identity Documents
    selfie = models.FileField(upload_to='documents/', blank=True)
    selfie_with_id = models.FileField(upload_to='documents/', blank=True)
    id_card = models.FileField(upload_to='documents/', blank=True)
    passport = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return self.username
