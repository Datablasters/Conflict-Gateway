from django.db import models
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
from django.contrib.flatpages.models import FlatPage
from django import forms
from tinymce.widgets import TinyMCE
from django.contrib.auth.models import User
import slugify

#Newsletter Model
class Newsletter(models.Model):
    email = models.CharField(max_length=200, unique=True)
    created = models.DateField('date published')

#News Model
class News(models.Model):
    user = models.ForeignKey(User)
    articletype = models.CharField(max_length=100, default="News")
    title = models.CharField(max_length=200, unique=True)
    created = models.DateField('date published')
    hits = models.IntegerField(default=0)
    tags = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200, default="news.jpg")
    tagline = models.CharField(max_length=500, default="Read more")
    website = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

# Articles Model
class Article(models.Model):
    user = models.ForeignKey(User)
    articletype = models.CharField(max_length=100, default="Article", editable=False)
    urlsection = models.CharField(max_length=100, default="articles", editable=False)
    title = models.CharField(max_length=200, unique=True)
    title_slug = models.CharField(max_length=200, unique=True)
    created = models.DateField('date published')
    author = models.CharField(max_length=100)
    authorimg = models.CharField(max_length=100, default="sebastian.png")
    hits = models.IntegerField(default=0, editable=False)
    tags = models.CharField(max_length=200)
    imgcredit = models.CharField(max_length=30)
    thumbnail = models.CharField(max_length=200, default="article.jpg")
    image = models.CharField(max_length=200, default = "article.jpg")
    tagline = models.CharField(max_length=500)
    body = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.title

# Training Material Model
class Training(models.Model):
    user = models.ForeignKey(User)
    articletype = models.CharField(max_length=100, default="Training", editable=False)
    urlsection = models.CharField(max_length=100, default="training", editable=False)
    title = models.CharField(max_length=200, unique=True)
    title_slug = models.CharField(max_length=200, unique=True)
    created = models.DateField('date published')
    author = models.CharField(max_length=100, default="View Training Material", editable=False)
    authorimg = models.CharField(max_length=100, default="trainingmaterial.png", editable=False)
    hits = models.IntegerField(default=0, editable=False)
    tags = models.CharField(max_length=200, default="Training Material", editable=False)
    imgcredit = models.CharField(max_length=30)
    thumbnail = models.CharField(max_length=200, default="training.jpg")
    image = models.CharField(max_length=200, default="training.jpg")
    tagline = models.CharField(max_length=500)
    body = tinymce_models.HTMLField()
    link = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.title

# Jobs Model
class Job(models.Model):
    user = models.ForeignKey(User)
    articletype = models.CharField(max_length=100, default="Jobs")
    urlsection = models.CharField(max_length=100, default="jobs")
    title = models.CharField(max_length=200, unique=True)
    title_slug = models.CharField(max_length=200, unique=True)
    created = models.DateField('date published')
    author = models.CharField(max_length=100, default = "Apply Online")
    authorimg = models.CharField(max_length=100, default="jobs.png")
    hits = models.IntegerField(default=0)
    tags = models.CharField(max_length=200, default="Mediation Jobs Conflict Resolution")
    location = models.CharField(max_length=30, default="Undesclosed")
    salary = models.CharField(max_length=30, default="Undesclosed")
    thumbnail = models.CharField(max_length=200, default="job.jpg")
    image = models.CharField(max_length=200, default="job.jpg")
    tagline = models.CharField(max_length=500)
    body = models.CharField(max_length=10000)
    link = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.title
