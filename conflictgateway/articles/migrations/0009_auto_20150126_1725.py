# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20150125_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='urlsection',
            field=models.CharField(default=b'articles', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='urlsection',
            field=models.CharField(default=b'jobs', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='training',
            name='urlsection',
            field=models.CharField(default=b'training', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='training',
            name='articletype',
            field=models.CharField(default=b'Training', max_length=100),
            preserve_default=True,
        ),
    ]
