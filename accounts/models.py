from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UnicodeUsernameValidator(RegexValidator):
    regex = r"^[\w.]+\Z"
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, and ./_ characters."
    )
    flags = 0

class User(AbstractUser):
  username_validator = UnicodeUsernameValidator()
  first_name = None
  last_name = None
  
  username = models.CharField(
    unique=True,
    max_length=30,
    validators=[username_validator],
  )
  email = models.EmailField(
    unique=True,
  )
  
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['email', ]

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  