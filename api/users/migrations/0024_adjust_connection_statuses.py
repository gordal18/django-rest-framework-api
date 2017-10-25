# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 12:14
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_create_users_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='requested', max_length=100, no_check_for_status=True, verbose_name='status'),
        ),
    ]
