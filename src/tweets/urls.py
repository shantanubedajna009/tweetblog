
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from .views import (TweetListView,
                    TweetDetailView,
                    TweetCreateView, 
                    TweetUpdateView, 
                    TweetDeleteView,
                    RetweetView)

app_name = "tweets"

urlpatterns = [
    url(r'^search/$', TweetListView.as_view(), name="list"),
    url(r'^$', RedirectView.as_view(url="/tweet/list/")),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail"),
    url(r'^create/$', TweetCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'),
    
]


