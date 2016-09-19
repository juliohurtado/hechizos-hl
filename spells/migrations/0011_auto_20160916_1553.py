# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0010_auto_20160916_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(choices=[('Neutrales', 'Neutrales'), ('Orden del F\xe9nix', 'Orden del F\xe9nix'), ('Marca Tenebrosa', 'Marca Tenebrosa'), ('Libro del Aprendiz de Brujo', 'Libro del Aprendiz de Brujo'), ('Libro de la Fortaleza', 'Libro de la Fortaleza'), ('Libro de la Sangre', 'Libro de la Sangre'), ('Libro del Equilibrio', 'Libro del Equilibrio'), ('Libro del Druida', 'Libro del Druida'), ('Libro del Caos', 'Libro del Caos'), ('Libro de los Ancestros', 'Libro de los Ancestros'), ('Libro de las Auras', 'Libro de las Auras'), ('Libro de Hermes Trimegisto', 'Libro de Hermes Trimegisto'), ('Libro de Merl\xedn', 'Libro de Merl\xedn')], max_length=64, unique=True),
        ),
    ]