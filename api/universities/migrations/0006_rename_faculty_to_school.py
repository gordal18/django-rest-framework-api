# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0005_remove_menu_from_university'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Faculty',
            new_name='School',
        ),
    ]
