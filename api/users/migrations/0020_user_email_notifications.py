# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_add_course_to_universities'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_notifications',
            field=models.BooleanField(default=True),
        ),
    ]
