from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.homepage, name='news-home'),                     # http://127.0.0.1:8000/
    path('event/', views.listevents, name='news_listevents'),       # http://127.0.0.1:8000/event/ for all events
    path('event/<int:pk>', views.event, name='news_event'),          # http://127.0.0.1:8000/event/<event_id> for individual events
    path('news/<int:pk>', views.newspost, name='news_newspost')     # http://127.0.0.1:8000/news/<primary_key> for specific newspost
]


from django.contrib.staticfiles.urls import staticfiles_urlpatterns     #Is used during dev for loading static files
urlpatterns += staticfiles_urlpatterns()