# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-02 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('range', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='spell',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spells.Type'),
        ),
    ]