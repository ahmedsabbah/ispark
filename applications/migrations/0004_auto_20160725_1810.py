# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-25 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_conference_contact_number'),
        ('applications', '0003_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('university', models.CharField(blank=True, max_length=200, null=True)),
                ('major', models.CharField(blank=True, max_length=200, null=True)),
                ('year_of_study_graduation', models.CharField(blank=True, max_length=200, null=True)),
                ('why_join', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('confirm_cv', models.BooleanField(default=False)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='services.Vacancy')),
            ],
            options={
                'verbose_name': 'Vacancy Application',
                'verbose_name_plural': 'Vacancy Applications',
            },
        ),
        migrations.AddField(
            model_name='conferenceapplication',
            name='wave',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
