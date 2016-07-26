# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-24 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_auto_20160720_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('A', 'Address'), ('E', 'Email'), ('P', 'Phone'), ('F', 'Facebook'), ('T', 'Twitter'), ('I', 'Instagram'), ('Y', 'Youtube'), ('D', 'Latitude'), ('G', 'Longitude')], max_length=1),
        ),
    ]