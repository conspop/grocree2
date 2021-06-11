from django.db import models
from django.contrib.auth.models import AbstractUser
from families.models import Family

class User(AbstractUser):
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE
    )
