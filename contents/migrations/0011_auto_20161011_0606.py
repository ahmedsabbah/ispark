# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-11 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_teammember_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidermain',
            name='join_now',
            field=models.CharField(choices=[('J', 'Join iSpark'), ('C', 'Conferences'), ('M', 'Major Exploration')], default='J', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slidermain',
            name='url',
            field=models.CharField(default='http://www.isparkegypt.com/', max_length=200),
            preserve_default=False,
        ),
    ]