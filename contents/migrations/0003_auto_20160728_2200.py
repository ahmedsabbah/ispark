# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-28 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_partner_slidersecondary_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slidersecondary',
            old_name='photo',
            new_name='logo',
        ),
        migrations.AddField(
            model_name='slidersecondary',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='partners'),
        ),
    ]
