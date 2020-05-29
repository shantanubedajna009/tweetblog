
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from tweets.api.views import (TweetListAPIView, 
                              TweetCreateAPIView, 
                              RetweetAPIView,
                              TweetLikeAPIView,
                              TweetDetailAPIView)


app_name = "tweet-api"

urlpatterns = [

     url(r'^$', TweetListAPIView.as_view(), name="list"), #tweet/api/tweet
     url(r'^create/$', TweetCreateAPIView.as_view(), name="create"),
     url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name="retweet"),
     url(r'^(?P<pk>\d+)/like/$', TweetLikeAPIView.as_view(), name="like"),
     url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name="detail"),

]
