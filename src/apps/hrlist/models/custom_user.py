from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import SoftDeletableModel

class CustomUser(SoftDeletableModel, AbstractUser):
    pass
