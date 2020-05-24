
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from tweets.api.views import TweetListAPIView


app_name = "accounts-api"

urlpatterns = [

    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name="list"),

]
