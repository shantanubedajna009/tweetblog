from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from hashtags.views import HashtagView

app_name = "tags"

urlpatterns = [

    url(r'^(?P<hashtag>.*)/$', HashtagView.as_view(), name="list"),
]