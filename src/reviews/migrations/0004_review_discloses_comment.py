# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20160307_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='discloses_comment',
            field=models.BooleanField(default=True, help_text='Whether the proposal submitter can read you comments. We will include your comments in the proposal acceptance/rejection notice sent to the submitter if you allow us to.', verbose_name='discloses comment to proposal submitter'),
        ),
    ]
