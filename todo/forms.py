from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
  text = forms.CharField()
  class Meta:
    model = Todo
    fields = ['text',]