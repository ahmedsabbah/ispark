# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0009_teammember_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='job',
            field=models.CharField(default='Doctor', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mentor',
            name='availability',
            field=models.TextField(blank=True, null=True),
        ),
    ]
