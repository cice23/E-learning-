from django.db import models
from lia.models import IntelligentLink

class Message(models.Model):
    """
    Represents a message received from a third-party service.
    """
    lia = models.ForeignKey(IntelligentLink, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender} - To: {self.lia.user.username} - Subject: {self.subject}"
