# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20161124_0040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='Home',
        ),
    ]