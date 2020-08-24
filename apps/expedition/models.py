from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Expedition(models.Model):
    """Represents a specific backpacking trip plan"""
    name = models.CharField(max_length=200, default='no title')
    slug = models.SlugField(max_length=200, null=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    goal = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, default='no description')
    date_published = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Expeditions"       # we will see this name in the admin page

    def __str__(self):
        """When referred to as a string, return self.title"""
        return self.name


class Task(models.Model):
    """Represents a specific task that is tied to an expedition"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='no description')
    plan = models.ForeignKey('Expedition', on_delete=models.CASCADE)