from django.db import models
from accounts.models import User

# Create your models here.

class Todo(models.Model):
  text = models.TextField()
  is_done = models.BooleanField(default=False)
  user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_todos')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)