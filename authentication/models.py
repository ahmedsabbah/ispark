from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    cv = models.FileField(upload_to='cvs', blank=True, null=True)
    coaching_progress = models.IntegerField(default=0)
    training_progress = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

class Badge(models.Model):
    TYPE_CHOICES = (
        ('T', 'University Tour'),
        ('I', 'Internship'),
        ('C', 'Conference')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, related_name='badges')

class Token(models.Model):
    user = models.OneToOneField(User, related_name='token')
    token = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
