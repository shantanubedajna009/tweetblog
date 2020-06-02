
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from hashtags.api.views import HastagListAPIView


app_name = "hashtags-api"

urlpatterns = [

    url(r'^(?P<hashtag>[\w.@+-]+)/$', HastagListAPIView.as_view(), name="list"),

]
