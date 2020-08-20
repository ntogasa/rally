from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Plan(models.Model):
    title = models.CharField(max_length=200, default='no title')
    leader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, default='no description')
    date_published = models.DateField(default=timezone.now)



