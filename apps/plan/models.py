from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=200, default='no name')
    leader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, default='no description')


