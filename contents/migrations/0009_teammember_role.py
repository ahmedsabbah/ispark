# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='role',
            field=models.CharField(choices=[('C', 'Core'), ('I', 'Intern')], default='C', max_length=1),
            preserve_default=False,
        ),
    ]