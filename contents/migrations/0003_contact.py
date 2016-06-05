# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-05 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20160603_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('A', 'Address'), ('E', 'Email'), ('P', 'Phone'), ('F', 'Facebook'), ('T', 'Twitter'), ('I', 'Instagram')], max_length=1)),
                ('value', models.CharField(max_length=300)),
            ],
        ),
    ]
