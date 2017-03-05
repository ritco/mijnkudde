# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 04:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schapen', '0003_auto_20170105_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schapen',
            name='vader',
        ),
        migrations.AddField(
            model_name='schapen',
            name='owner',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schapen',
            name='pub_datum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schapen',
            name='vater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vaters', to='schapen.Schapen'),
        ),
        migrations.AlterField(
            model_name='schapen',
            name='moeder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moeders', to='schapen.Schapen'),
        ),
    ]
