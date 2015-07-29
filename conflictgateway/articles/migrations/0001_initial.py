# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('title_slug', models.CharField(unique=True, max_length=200)),
                ('created', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('hits', models.IntegerField(default=0)),
                ('tags', models.CharField(max_length=200)),
                ('continent', models.CharField(max_length=30)),
                ('thumbnail', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=500)),
                ('body', models.CharField(max_length=10000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
