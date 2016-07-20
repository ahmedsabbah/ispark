from __future__ import unicode_literals
from django.db import models

class TourApplication(models.Model):
    KNOW_CHOICES = (
        ('FB', 'Facebook'),
        ('FR', 'Friend'),
        ('YS', 'Your School'),
        ('OW', 'Our Website'),
        ('PE', 'Previous Event')
    )
    tour = models.ForeignKey('services.Tour', related_name='applications')
    majors = models.ManyToManyField('contents.Major', related_name='tour_applications', blank=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    grade_level = models.CharField(max_length=200, blank=True, null=True)
    wave = models.CharField(max_length=200, blank=True, null=True)
    joined_previous_event = models.BooleanField(default=False)
    previous_event = models.CharField(max_length=200, blank=True, null=True)
    know_about_us = models.CharField(max_length=2, choices=KNOW_CHOICES)
    class Meta:
        verbose_name = 'Tour Application'
        verbose_name_plural = 'Tour Applications'
    def __str__(self):
        return self.name

class ConferenceApplication(models.Model):
    KNOW_CHOICES = (
        ('FB', 'Facebook'),
        ('FR', 'Friend'),
        ('YS', 'Your School'),
        ('OW', 'Our Website'),
        ('PE', 'Previous Event')
    )
    conference = models.ForeignKey('services.Conference', related_name='applications')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    grade_level = models.CharField(max_length=200, blank=True, null=True)
    # wave = models.CharField(max_length=200)
    payment = models.TextField(blank=True, null=True)
    joined_previous_event = models.NullBooleanField()
    previous_event = models.CharField(max_length=200, blank=True, null=True)
    know_about_us = models.CharField(max_length=2, choices=KNOW_CHOICES)
    class Meta:
        verbose_name = 'Conference Application'
        verbose_name_plural = 'Conference Applications'
    def __str__(self):
        return self.name
