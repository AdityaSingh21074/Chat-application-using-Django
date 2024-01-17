from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms
# from .models import Room

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# class CreateRoomForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         fields = ['name', 'slug']