from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from models import Article, Training, Job, News, Newsletter
from datetime import datetime
from itertools import chain
from operator import attrgetter

# Create your views here.
def custom_404(request):
    return render(request, '404.html')

@csrf_exempt
def newsletter(request):
    if request.is_ajax():
        if request.POST:
            useremail = request.POST.get('email')
            match = re.search(r'[\w.-]+@[\w.-]+.\w+', useremail)
            if match:
                signup = Newsletter(email=useremail, created=datetime.utcnow())
                signup.save()
            news_list = News.objects.order_by('-created')
            article_list = Article.objects.order_by('-created')
            jobs_list = Job.objects.order_by('-created')
            training_list = Training.objects.order_by('-created')
            context = {'news_list': news_list, 'article_list': article_list,
            'jobs_list': jobs_list, 'training_list': training_list}
            return render(request, 'index.html', context)
    else:
        news_list = News.objects.order_by('-created')
        article_list = Article.objects.order_by('-created')
        jobs_list = Job.objects.order_by('-created')
        training_list = Training.objects.order_by('-created')
        context = {'news_list': news_list, 'article_list': article_list,
               'jobs_list': jobs_list, 'training_list': training_list}
        return render(request, 'index.html', context)


def index(request):
    news_list = News.objects.order_by('-created')
    article_list = Article.objects.order_by('-created')
    jobs_list = Job.objects.order_by('-created')
    training_list = Training.objects.order_by('-created')
    #Combine queries into once response
    contents_list = sorted(chain(article_list, training_list, news_list, jobs_list), key=attrgetter('created'),
                           reverse=True)
    template = "index.html"
    context = {'contents_list': contents_list}
    return render(request, template, context)

def newsindex(request):
    article_list = News.objects.order_by('-created')
    template = 'newsindex.html'
    context = {'article_list': article_list}
    return render(request, template, context)

def articleindex(request):
    article_list = Article.objects.order_by('-created')
    template = 'articlesindex.html'
    context = {'article_list': article_list}
    return render(request, template, context)

def jobsindex(request):
    article_list = Job.objects.order_by('-created')
    template = 'jobsindex.html'
    context = {'article_list':article_list}
    return render(request, template, context)

def trainingindex(request):
    article_list = Training.objects.order_by('-created')
    template = 'trainingindex.html'
    context = {'article_list':article_list}
    return render(request, template, context)

def directoryindex(request):
    article_list = Article.objects.order_by('-created')
    context = {'article_list':article_list}
    return render(request, 'directoryindex.html', context)

def article(request, title_slug):
    try:
        article = Article.objects.get(title_slug = title_slug)
    except Article.DoesNotExist:
        raise Http404("Page does not exist")
    try:
        article_hot = Article.objects.order_by('hits')[:5]
    except:
        pass
    return render(request, 'articles.html', {'article':article,
                                             'article_hot':article_hot})

def training(request, title_slug):
    try:
        article = Training.objects.get(title_slug = title_slug)
    except Article.DoesNotExist:
        raise Http404("Page does not exist")
    try:
        article_hot = Training.objects.order_by('hits')[:5]
    except:
        pass
    return render(request, 'training.html', {'article': article,
                                             'article_hot': article_hot})

def jobs(request, title_slug):
    try:
        article = Job.objects.get(title_slug=title_slug)
    except Article.DoesNotExist:
        raise Http404("Page does not exist")
    try:
        article_hot = Job.objects.order_by('hits')[:5]
    except:
        pass
    return render(request, 'job.html', {'article': article,
                                        'article_hot': article_hot})

def directory(request, title_slug):
    try:
        article = Directory.objects.get(title_slug=title_slug)
    except Article.DoesNotExist:
        raise Http404("Page does not exist")
    try:
        article_hot = Article.objects.order_by('hits')[:5]
    except:
        pass
    return render(request, 'directory.html', {'article': article,
                                              'article_hot': article_hot})


