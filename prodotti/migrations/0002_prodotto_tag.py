# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodotto',
            name='tag',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]