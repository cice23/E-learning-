import uuid
from django.db import models
from users.models import User

class IntelligentLink(models.Model):
    """
    Represents an Intelligent Link for Anonymous (LIA) registration.
    """
    class LinkLevel(models.TextChoices):
        WEAK = 'WEAK', 'Weak'
        MEDIUM = 'MEDIUM', 'Medium'
        STRONG = 'STRONG', 'Strong'

    class LinkStatus(models.TextChoices):
        GENERATED = 'GENERATED', 'Generated'
        USED = 'USED', 'Used'
        EXPIRED = 'EXPIRED', 'Expired'
        REVOKED = 'REVOKED', 'Revoked'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    level = models.CharField(max_length=10, choices=LinkLevel.choices)
    status = models.CharField(max_length=10, choices=LinkStatus.choices, default=LinkStatus.GENERATED)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"{self.service_name} ({self.get_level_display()}) - {self.user.username}"
