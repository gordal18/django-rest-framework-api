# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_rename_post_comment_to_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='faculty',
            new_name='school',
        ),
    ]
