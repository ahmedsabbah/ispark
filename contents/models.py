from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='categories')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
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
    photo = models.ImageField(upload_to='universities')
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='mentors')
    areas_of_expertise = models.ManyToManyField('contents.Category', related_name='mentors', blank=True)
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
    photo = models.ImageField(upload_to='team')
    position = models.CharField(max_length=200)
    quote = models.TextField()
    email = models.EmailField()
    profile = models.FileField(upload_to='team', blank=True, null=True)
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    def __str__(self):
        return self.name

class Contact(models.Model):
    TYPE_CHOICES = (
        ('AD', 'Address'),
        ('EM', 'Email'),
        ('PH', 'Phone'),
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('IN', 'Instagram'),
        ('YT', 'Youtube'),
        ('LT', 'Latitude'),
        ('LG', 'Longitude'),
        ('PP', 'Phone Students and Parents'),
        ('PS', 'Phone Schools'),
        ('PU', 'Phone Universities'),
        ('PC', 'Phone Companies')
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    value = models.CharField(max_length=300)
    class Meta:
        verbose_name = 'Contact Info Item'
        verbose_name_plural = 'Contact Info'
    def __str__(self):
        return self.type

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'
    def __str__(self):
        return self.title

class Job(models.Model):
    category = models.ForeignKey('contents.Category', related_name='jobs')
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='jobs')
    description = models.TextField()
    interests = models.ManyToManyField('contents.Skill', related_name='jobs', blank=True)
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    def __str__(self):
        return self.title

class JobSkill(models.Model):
    job = models.ForeignKey(Job, related_name='skills')
    skill = models.ForeignKey('contents.Skill', related_name='job_skills')
    value = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Job Skill'
        verbose_name_plural = 'Job Skills'
    def __str__(self):
        return self.skill.name

class Partner(models.Model):
    TYPE_CHOICES = (
        ('AD', 'Address'),
        ('EM', 'Email'),
        ('PH', 'Phone')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='partners')
    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='partners')
    text = models.TextField()
    video_link = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    def __str__(self):
        return self.name

class SliderSecondary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    logo = models.ImageField(upload_to='partners')
    background = models.ImageField(upload_to='partners')
    class Meta:
        verbose_name = 'Slider Secondary'
        verbose_name_plural = 'Sliders Secondary'
    def __str__(self):
        return self.title
