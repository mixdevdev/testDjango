from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# inherit class AbstractUser to override and add fields in user

class User(AbstractUser):
    profile_photo=models.ImageField(verbose_name="Profile photo")