# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-10 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_auto_20160909_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(choices=[('S', 'School'), ('U', 'University'), ('C', 'Company'), ('O', 'Organization')], max_length=1),
        ),
    ]