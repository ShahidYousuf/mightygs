# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20180222_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optiona', models.CharField(max_length=50)),
                ('optionb', models.CharField(max_length=50)),
                ('optionc', models.CharField(max_length=50)),
                ('optiond', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('sections', models.ManyToManyField(to='restapp.Section')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='optiona',
        ),
        migrations.RemoveField(
            model_name='question',
            name='optionb',
        ),
        migrations.RemoveField(
            model_name='question',
            name='optionc',
        ),
        migrations.RemoveField(
            model_name='question',
            name='optiond',
        ),
        migrations.AddField(
            model_name='section',
            name='questions',
            field=models.ManyToManyField(to='restapp.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(to='restapp.Answer'),
        ),
    ]
