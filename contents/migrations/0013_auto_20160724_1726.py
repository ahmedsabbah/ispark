# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-24 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0012_auto_20160724_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='areas_of_expertise',
            field=models.ManyToManyField(blank=True, related_name='mentors', to='contents.Category'),
        ),
    ]