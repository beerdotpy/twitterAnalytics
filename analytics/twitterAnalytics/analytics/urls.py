from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^index/table/$', views.tweet_by_list, name='tweet_by_list'),
    url(r'^index/pie/', views.tweet_by_location, name='tweet_by_location'),
    url(r'^index/line/', views.tweet_by_count, name='tweet_by_count'),
]