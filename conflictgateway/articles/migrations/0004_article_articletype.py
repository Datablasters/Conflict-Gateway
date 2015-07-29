# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_authorimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articletype',
            field=models.CharField(default=b'Article', max_length=100),
            preserve_default=True,
        ),
    ]
