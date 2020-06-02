from rest_framework.generics import ListAPIView
from rest_framework import permissions
from tweets.models import Tweet
from tweets.api.serializers import TweetModelSerializer
from django.db.models import Q
from tweets.api.pagination import StandardResultsPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from hashtags.models import HashTag


class HastagListAPIView(ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [permissions.AllowAny]


    # standard for this too as the Listview itself
    # cause to get liked by us or not to change the verb we need to
    # add requested_user for the get_liked_by_user method in the serializer
    # just modifying the context view of a APIView
    def get_serializer_context(self, *args, **kwargs):
        context = super(HastagListAPIView, self).get_serializer_context(*args, **kwargs)
        context['requested_user'] = self.request

        return context


    def get_queryset(self, *args, **kwargs):
        
        #requested_user = self.kwargs.get("username") 

        hashtag = self.kwargs.get("hashtag")


        qs = None

        if hashtag:

            tag_obj, created_or_not = HashTag.objects.get_or_create(tag=hashtag)

            if tag_obj:    

                # qs is now list of tweets that has that specific hastag in their content
                qs = tag_obj.tag_tweets()

                if qs.exists():
                    qs = qs.order_by("-timestamp")    
            
            # pretty self explanatory
            # just checking if q is present
            
            q = self.request.GET.get("q", None)
            
            if q and qs:
                qs = qs.filter(
                    Q(content__icontains=q) |
                    Q(user__username__icontains=q)
            )



        return qs