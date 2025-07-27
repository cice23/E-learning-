from rest_framework import serializers
from .models import IntelligentLink

class LiaVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntelligentLink
        fields = ['token', 'level', 'status']

class LiaValidationSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    domain = serializers.CharField(max_length=255)
    level_required = serializers.ChoiceField(choices=IntelligentLink.LinkLevel.choices)
