# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-09 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_auto_20160728_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(choices=[('S', 'School'), ('U', 'University'), ('C', 'Company')], max_length=1),
        ),
    ]
