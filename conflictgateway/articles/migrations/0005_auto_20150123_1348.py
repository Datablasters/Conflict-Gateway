# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_article_articletype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articletype', models.CharField(default=b'Training Material', max_length=100)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('title_slug', models.CharField(unique=True, max_length=200)),
                ('created', models.DateField()),
                ('author', models.CharField(default=b'View Training Material', max_length=100)),
                ('authorimg', models.CharField(default=b'trainingmaterial.png', max_length=100)),
                ('hits', models.IntegerField(default=0)),
                ('tags', models.CharField(default=b'Training Material', max_length=200)),
                ('imgcredit', models.CharField(max_length=30)),
                ('thumbnail', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=500)),
                ('body', models.CharField(max_length=10000)),
                ('link', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='articletype',
            field=models.CharField(default=b'Articles', max_length=100),
            preserve_default=True,
        ),
    ]
