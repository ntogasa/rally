from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Expedition(models.Model):
    title = models.CharField(max_length=200, default='no title')
    leader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, default='no description')
    date_published = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Plans"       # we will see this name in the admin page

    def __str__(self):
        """When referred to as a string, return self.title"""
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='no description')
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)


