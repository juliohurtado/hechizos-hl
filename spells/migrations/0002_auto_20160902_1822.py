# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-02 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='range',
        ),
        migrations.AddField(
            model_name='spell',
            name='range',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
