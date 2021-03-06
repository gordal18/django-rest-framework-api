# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0009_remove_id_from_field_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('action', models.CharField(choices=[('reported', 'Reported'), ('hidden', 'Hidden'), ('cleared', 'Cleared'), ('edited', 'Edited'), ('userdeleted', 'Delete by user')], max_length=20)),
                ('comment', models.CharField(blank=True, max_length=80)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='reportedpost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='reportedpost',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='ReportedPost',
        ),
    ]
