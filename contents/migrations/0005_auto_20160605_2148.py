# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-05 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_auto_20160605_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
