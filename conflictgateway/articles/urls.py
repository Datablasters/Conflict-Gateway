from django.conf.urls import patterns, url
from articles import views

handler404 = 'articles.views.custom_404'

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
                           url(r'^features/(?P<title_slug>[-\w]+)/$', views.article, name ='article'),
                           url(r'^jobs/(?P<title_slug>[-\w]+)/$', views.jobs, name ='jobs'),
                           url(r'^training/(?P<title_slug>[-\w]+)/$', views.training, name ='training'),
                           url(r'^directory/(?P<title_slug>[-\w]+)/$', views.directory, name ='directory'),
                           url(r'^news/$', views.newsindex, name ='newsindex'),
                           url(r'^features/$', views.articleindex, name ='articleindex'),
                           url(r'^jobs/$', views.jobsindex, name ='jobsindex'),
                           url(r'^training/$', views.trainingindex, name ='trainingindex'),
                           url(r'^directory/$', views.directoryindex, name ='directoryindex'),
                           url(r'^newsletter/$', views.newsletter, name='newsletter'),
                      )