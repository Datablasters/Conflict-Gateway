# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20150125_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tagline',
            field=models.CharField(default=b'Read more', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.CharField(default=b'news.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='training',
            name='created',
            field=models.DateField(verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
