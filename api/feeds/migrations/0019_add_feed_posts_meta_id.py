# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0018_post_targeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feed_posts_meta_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(blank=True, default='post', max_length=12, null=True),
        ),
    ]