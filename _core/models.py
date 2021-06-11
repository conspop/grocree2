from django.db import models
from families.models import Family

class Profile(models.Model):
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE
    )
