# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-11 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_auto_20180611_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='last_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='user1',
            name='password',
            field=models.CharField(default='password', max_length=50),
        ),
    ]
