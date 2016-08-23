from __future__ import unicode_literals
from django.db import models


class Tour(models.Model):
    university = models.ForeignKey('contents.University', related_name='tours')
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    transportation = models.BooleanField()
    age_range = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    fb_link = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
    def __str__(self):
        return self.university.name

class Major(models.Model):
    tour = models.ForeignKey('services.Tour', related_name='majors')
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'
    def __str__(self):
        return self.name

class Conference(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='conferences')
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    fb_link = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Conference'
        verbose_name_plural = 'Conferences'
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    TYPE_CHOICES = (
        ('I', 'Internship'),
        ('J', 'Job')
    )
    role = models.CharField(max_length=1, choices=TYPE_CHOICES)
    position = models.CharField(max_length=200)
    description = models.TextField()
    contact_email = models.EmailField()
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
    def __str__(self):
        return '%s (%s)' % (self.position, self.role)


class Opportunity(models.Model):
    TYPE_CHOICES = (
        ('I', 'Internship'),
        ('J', 'Job Shadowing')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    job_title = models.CharField(max_length=200)
    industry = models.ForeignKey('contents.Category', related_name='opportunities')
    posted_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    employer = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='opportunities')
    location = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunities'
    def __str__(self):
        return '%s (%s)' % (self.job_title, self.type)

class OpportunityRequirement(models.Model):
    text = models.TextField()
    opportunity = models.ForeignKey('services.Opportunity', related_name='requirements')
    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'
    def __str__(self):
        return self.text
