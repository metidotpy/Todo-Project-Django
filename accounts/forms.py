from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from .models import User

class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

