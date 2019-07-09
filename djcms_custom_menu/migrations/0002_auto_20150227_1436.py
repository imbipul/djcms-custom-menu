# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djcms_custom_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='djcmscustommenu',
            options={'verbose_name': 'DJCMS Custom Menu', 'verbose_name_plural': 'DJCMS Custom Menu'},
        ),
    ]
