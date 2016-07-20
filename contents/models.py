from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('contents.Category', related_name='majors')
    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='universities', blank=True, null=True)
    photo = models.ImageField(upload_to='universities', blank=True, null=True)
    majors = models.ManyToManyField('contents.Major', related_name='universities')
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='mentors', blank=True, null=True)
    areas_of_expertise = models.ManyToManyField('contents.Major', related_name='mentors', blank=True)
    availability = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentors'
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    ROLE_CHOICES = (
        ('C', 'Core'),
        ('I', 'Intern')
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team', blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    quote = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    def __str__(self):
        return self.name

class Contact(models.Model):
    TYPE_CHOICES = (
        ('A', 'Address'),
        ('E', 'Email'),
        ('P', 'Phone'),
        ('F', 'Facebook'),
        ('T', 'Twitter'),
        ('I', 'Instagram'),
        ('D', 'Latitude'),
        ('G', 'Longitude')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    value = models.CharField(max_length=300)
    class Meta:
        verbose_name = 'Contact Info Item'
        verbose_name_plural = 'Contact Info'
    def __str__(self):
        return self.type

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'
    def __str__(self):
        return self.title
