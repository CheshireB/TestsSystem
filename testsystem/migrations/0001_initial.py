# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.IntegerField(default=-1)),
                ('task', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('flag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.IntegerField(default=-1)),
                ('task', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('id_test', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='temp_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_test', models.IntegerField()),
                ('id_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsystem.tasks')),
            ],
        ),
        migrations.AddField(
            model_name='comment_task',
            name='id_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsystem.tasks'),
        ),
    ]