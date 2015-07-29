# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('created', models.DateTimeField(verbose_name=b'date published')),
                ('hits', models.IntegerField(default=0)),
                ('tags', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(default=b'article.jpg', max_length=200)),
                ('website', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(default=b'article.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.CharField(default=b'article.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='author',
            field=models.CharField(default=b'Apply Online', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.CharField(default=b'job.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=models.CharField(default=b'Mediation Jobs Conflict Resolution', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='thumbnail',
            field=models.CharField(default=b'job.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='training',
            name='created',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='training',
            name='image',
            field=models.CharField(default=b'training.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='training',
            name='thumbnail',
            field=models.CharField(default=b'training.jpg', max_length=200),
            preserve_default=True,
        ),
    ]
