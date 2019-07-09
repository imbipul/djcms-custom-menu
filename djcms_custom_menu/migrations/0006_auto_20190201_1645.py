# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 16:45
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djcms_custom_menu', '0005_auto_20181204_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djcmscustommenu',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
