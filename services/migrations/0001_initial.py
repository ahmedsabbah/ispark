# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='conferences')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('contact_number', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Conference',
                'verbose_name_plural': 'Conferences',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('I', 'Internship'), ('J', 'Job Shadowing')], max_length=1)),
                ('job_title', models.CharField(max_length=200)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('employer', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='opportunities')),
                ('location', models.CharField(max_length=200)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='contents.Category')),
            ],
            options={
                'verbose_name': 'Opportunity',
                'verbose_name_plural': 'Opportunities',
            },
        ),
        migrations.CreateModel(
            name='OpportunityRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='services.Opportunity')),
            ],
            options={
                'verbose_name': 'Requirement',
                'verbose_name_plural': 'Requirements',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('transportation', models.BooleanField()),
                ('age_range', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=15)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='contents.University')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('I', 'Internship'), ('J', 'Job')], max_length=1)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.AddField(
            model_name='major',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majors', to='services.Tour'),
        ),
    ]
