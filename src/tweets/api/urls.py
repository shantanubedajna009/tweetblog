
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from tweets.api.views import (TweetListAPIView, TweetCreateAPIView)


app_name = "tweet-api"

urlpatterns = [

     url(r'^$', TweetListAPIView.as_view(), name="list"), #tweet/api/tweet
     url(r'^create/$', TweetCreateAPIView.as_view(), name="create"),

]
