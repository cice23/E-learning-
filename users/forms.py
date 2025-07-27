from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms
from .models import User

class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['selfie', 'selfie_with_id', 'id_card', 'passport']
