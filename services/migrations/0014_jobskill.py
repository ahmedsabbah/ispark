# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-27 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20160727_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='services.Job')),
            ],
        ),
    ]
