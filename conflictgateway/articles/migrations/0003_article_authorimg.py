# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150121_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authorimg',
            field=models.CharField(default=b'sebastian.png', max_length=100),
            preserve_default=True,
        ),
    ]
