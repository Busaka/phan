# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schools',
            new_name='School',
        ),
    ]
