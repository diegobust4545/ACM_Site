# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm_committee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='committeepage',
            old_name='committe_bio',
            new_name='committee_bio',
        ),
        migrations.RenameField(
            model_name='committeepage',
            old_name='committe_title',
            new_name='committee_title',
        ),
    ]
