from django.shortcuts import render
from .models import Post, Event, Slideshow
from datetime import date, timedelta
from django.apps import apps

Job = apps.get_model('users', 'Job')


def homepage(request):
    context = {
        'posts': Post.objects.all()[:12],                           # 'Post' is a model in news/models.py
        'events': Event.objects.order_by('event_time')[:4],         # 'Event' is a model in news/models.py
        'jobs': Job.objects.all()[:5],                              # 'Job' is a model in jobs/models.py
        'slideshow_init': Slideshow.objects.all(),                  # 'Slideshow' is a model i news/models.py
        'slideshow': Slideshow.objects.all()[1:]
    }
    return render(request, 'news/homepage.html', context)


def newspost(request, pk):
    context = {
        'newspost': Post.objects.get(pk=pk)
    }
    return render(request, 'news/post.html', context)


def listevents(request):
    today = date.today()
    one_year_away = today + timedelta(weeks=51)
    events = Event.objects.filter(event_time__gte=today, event_time__lte=
        one_year_away).order_by('event_time')


    context = {
        'events': events
    }

    return render(request, 'news/listevents.html', context)


def event(request, pk):
    context = {
        'event': Event.objects.get(pk=pk)
    }
    return render(request, 'news/event.html', context)


