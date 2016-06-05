from __future__ import unicode_literals
from django.db import models


class Tour(models.Model):
    university = models.ForeignKey('contents.University', related_name='tours')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    transportation = models.NullBooleanField(blank=True, null=True)
    age_range = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    majors = models.ManyToManyField('contents.Major', related_name='tours', blank=True)
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
    def __str__(self):
        return self.university.name

class Conference(models.Model):
    name = models.CharField(max_length=200) # check if really needed
    photo = models.ImageField(upload_to='conferences', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name = 'Conference'
        verbose_name_plural = 'Conferences'
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    TYPE_CHOICES = (
        ('I', 'Internship'),
        ('P', 'Part Time'),
        ('F', 'Full Time')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    role = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='vacancies', blank=True, null=True)
    internship_type = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    working_days = models.CharField(max_length=200, blank=True, null=True)
    working_hours = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
    def __str__(self):
        return '%s (%s)' % (self.role, self.type)

class VacancyRequirement(models.Model):
    text = models.TextField()
    vacancy = models.ForeignKey('services.Vacancy', related_name='requirements')
    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'
    def __str__(self):
        return self.text

class Opportunity(models.Model):
    TYPE_CHOICES = (
        ('I', 'Internship'),
        ('J', 'Job Shadowing')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    job_title = models.CharField(max_length=200)
    internship_type = models.CharField(max_length=200, blank=True, null=True)
    industry = models.ForeignKey('contents.Category', related_name='opportunities', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
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


# class Wave(models.Model):
#     title = models.CharField(max_length=200)
#     class Meta:
#         verbose_name = 'Wave'
#         verbose_name_plural = 'Waves'
#     def __str__(self):
#         return self.title
