# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0014_set_default_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlog',
            name='comment',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]