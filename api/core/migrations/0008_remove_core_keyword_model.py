# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 03:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_category_fields'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Keyword',
        ),
    ]
