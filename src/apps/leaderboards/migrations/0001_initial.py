# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-02 19:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0005_competitionparticipant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('competition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leaderboard', to='competitions.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default=django.utils.timezone.now, max_length=50)),
                ('key', models.CharField(max_length=10, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_metrics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='column',
            name='leaderboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='leaderboards.Leaderboard'),
        ),
        migrations.AddField(
            model_name='column',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='leaderboards.Metric'),
        ),
    ]
