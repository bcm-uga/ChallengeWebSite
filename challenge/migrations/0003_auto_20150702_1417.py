# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20150702_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
