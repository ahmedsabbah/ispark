# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20160720_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='internship_type',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]