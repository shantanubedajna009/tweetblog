from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import home
from tweets.views import TweetListView
from accounts.views import UserRegisterView
from django.contrib.auth.views import LoginView, LogoutView

import os

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name="home"),


    url(r'^register/$', UserRegisterView.as_view(), name='register'), 
    url(r'^login/$', LoginView.as_view(), {'template_name': 'registration/login.html'}, name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),


    url(r'^tweet/', include('tweets.urls', namespace="tweets")),
    url(r'^', include('accounts.urls', namespace="accounts")),
    url(r'^api/tweet/', include('tweets.api.urls', namespace="tweet-api")),
    url(r'^api/', include('accounts.api.urls', namespace="accounts-api")),
    url(r'^api/tag/', include('hashtags.api.urls', namespace="hashtags-api")),
    url(r'^tags/', include('hashtags.urls', namespace='tags')),

]

urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
