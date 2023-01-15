from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AlertUserProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=16)
    lucky_number = models.IntegerField()