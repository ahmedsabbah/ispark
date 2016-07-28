from __future__ import unicode_literals
from django.db import models
from authentication.models import Profile

class TourApplication(models.Model):
    KNOW_CHOICES = (
        ('FB', 'Facebook'),
        ('FR', 'Friend'),
        ('YS', 'Your School'),
        ('OW', 'Our Website'),
        ('PE', 'Previous Event')
    )
    tour = models.ForeignKey('services.Tour', related_name='applications')
    majors = models.ManyToManyField('services.Major', related_name='tour_applications', blank=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    school_name = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=200)
    wave = models.CharField(max_length=200)
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
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    school_name = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=200)
    wave = models.CharField(max_length=200)
    payment = models.TextField(blank=True, null=True)
    joined_previous_event = models.BooleanField(default=False)
    previous_event = models.CharField(max_length=200, blank=True, null=True)
    know_about_us = models.CharField(max_length=2, choices=KNOW_CHOICES)
    class Meta:
        verbose_name = 'Conference Application'
        verbose_name_plural = 'Conference Applications'
    def __str__(self):
        return self.name

class VacancyApplication(models.Model):
    vacancy = models.ForeignKey('services.Vacancy', related_name='applications')
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    university = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    year_of_study_graduation = models.CharField(max_length=200)
    why_join = models.TextField()
    experience = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Vacancy Application'
        verbose_name_plural = 'Vacancy Applications'
    def __str__(self):
        return self.name

class OpportunityApplication(models.Model):
    opportunity = models.ForeignKey('services.opportunity', related_name='applications')
    user = models.ForeignKey(Profile, related_name='opportunity_applications')
    submitted_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Opportunity Application'
        verbose_name_plural = 'Opportunity Applications'
    def __str__(self):
        return '%s %s' % (self.user.user.first_name, self.user.user.last_name)
