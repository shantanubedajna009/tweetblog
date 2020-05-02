from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions
from tweets.models import Tweet
from tweets.api.serializers import TweetModelSerializer
from django.db.models import Q
from tweets.api.pagination import StandardResultsPagination



class TweetCreateAPIView(CreateAPIView):
    
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(ListAPIView):
    
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        
        user_instance = self.request.user # ekhane self.request.user holo User class instance of current logged in User
        user_profile = user_instance.profile # back tracing from User class's foreign key coming to UserProfile by using related_name
        
        # One to one relationship so getting one data only

        #users_im_following = user_profile.following.all() # Returns all following Users Including Me
        
        users_im_following = user_profile.get_following() # method we have set up in the UserProfile class

        # filters User that is not Me cause same user ME is present in both User and Userprofile 
        
        qs = Tweet.objects.filter(user__in=users_im_following) # basically SQL nested Query with the IN to compare with more than one fields
        
        qs2 = Tweet.objects.filter(user=self.request.user)
        qs = (qs | qs2).distinct()
        
        qs = qs.order_by("-timestamp")
        
        
        # pretty self explanatory
        # just checking if q is present
        
        q = self.request.GET.get("q", None)
        
        if q:
            qs = qs.filter(
                Q(content__icontains=q) |
                Q(user__username__icontains=q)
            )
        return qs
