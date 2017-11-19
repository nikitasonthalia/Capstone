# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_eventscategory_eventsuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('offers', models.CharField(max_length=50)),
                ('package', models.CharField(max_length=50)),
                ('serviceDetails', models.CharField(max_length=50)),
                ('productDescription', models.CharField(max_length=50)),
                ('aboutProduct', models.CharField(max_length=50)),
                ('aboutUs', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='search.UserProfile')),
            ],
        ),
    ]
