# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 04:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_merge_20170207_0042'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroupmember',
            name='non_ucroo_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.NonMember'),
        ),
        migrations.AddField(
            model_name='studygroupmember',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studygroupmember',
            name='invited_by_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
