# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 22:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20170131_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_fb_page_id',
            new_name='fb_page_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_is_international',
            new_name='is_international',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_uni',
            new_name='uni',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_year',
            new_name='year',
        ),
    ]
