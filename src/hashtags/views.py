from django.shortcuts import render
from django.views import View
from hashtags.models import HashTag

class HashtagView(View):

    # for when we use a View in get method the url parameter get's passed like this
    # in the next argument to request itself

    def get(self, request, hashtag, *args, **kwargs):
        obj, created_or_not = HashTag.objects.get_or_create(tag=hashtag) # no # cause the url parameter comes without #

        return render(request, 'hashtags/list_view.html', context={'obj': obj})



