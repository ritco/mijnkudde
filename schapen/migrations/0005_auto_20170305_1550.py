# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schapen', '0004_auto_20170305_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schapen',
            name='vater',
        ),
        migrations.AddField(
            model_name='schapen',
            name='vader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vaders', to='schapen.Schapen'),
        ),
    ]
