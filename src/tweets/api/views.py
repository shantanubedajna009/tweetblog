from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions
from tweets.models import Tweet
from tweets.api.serializers import TweetModelSerializer
from django.db.models import Q
from tweets.api.pagination import StandardResultsPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin




class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):

        message = ""  # leaving message blank cause the 
        # permission class auto sens a message
        # if the user is not authenticated


        # we did filter here because get throws an error 
        # wiich is not auto handled by rest_framework like djngo views
        tweet_qs = Tweet.objects.filter(pk=pk)

        # just some syntactical suger to get the first object
        if tweet_qs.exists():

            if tweet_qs.count() == 1:
            
                message = "Can't tweet more in one day"

                new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
                
                if new_tweet:
                    
                    serialized_data = TweetModelSerializer(new_tweet) 
                    #serialized_data.update()
                    # Serializers 
                    # actually works like this CBVs just handle it behind the scenes 
                    #serialized_data
                    #new_dict = {'requested_user': self.request.user}
                    #print('\n\n\n', self.request.user, '\n\n\n')

                    #new_dict.update(serialized_data.data)

                    return Response(data=serialized_data.data)
            else:
                message = "FUCK!! MORE THAN ONE TWEET IS THERE WIT SAME PK"

        return Response({"message": message}, status=400)



class TweetLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):

        tweet_qs = Tweet.objects.filter(pk=pk)

        if tweet_qs.exists() and tweet_qs.count() == 1:
            
            is_liked, count = Tweet.objects.toggle_like(request.user, tweet_qs.first()) 

            # we dont need to serialize a model here just returning a json response
            # through the API
            return Response({"is_liked": is_liked, "count": count})

        return Response({"message": "OOPS SOmething Went wrong !"}, status=400)


class TweetCreateAPIView(CreateAPIView):
    
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    # just modifying the context view of a APIView
    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetCreateAPIView, self).get_serializer_context(*args, **kwargs)
        context['requested_user'] = self.request

        return context


    # eta karon user ta by default aashe naa 
    # jokhon $(this).serialize() use korchi jquery te 
    # form er data take nie json banie
    # tarpor , serializer er through pathacche
    # tai manually request.user ta attach korte hocce
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    


class TweetDetailAPIView(ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [permissions.AllowAny]


    # standard for this too as the Listview itself
    # cause to get liked by us or not to change the verb we need to
    # add requested_user for the get_liked_by_user method in the serializer
    # just modifying the context view of a APIView
    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetDetailAPIView, self).get_serializer_context(*args, **kwargs)
        context['requested_user'] = self.request

        return context


    def get_queryset(self, *args, **kwargs):
        
        requested_user = self.kwargs.get("username") 

        pk_of = self.kwargs.get("pk")

        qs = Tweet.objects.filter(pk=pk_of)

        if qs.exists() and qs.count() == 1:
            twt = qs.first()

            twt_chil = Tweet.objects.get_reply_children(twt)

            if twt_chil.exists():
                qs = (qs | twt_chil).distinct()
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



class TweetListAPIView(ListAPIView):
    
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [permissions.AllowAny]

    
    # just modifying the context view of a APIView
    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['requested_user'] = self.request

        return context


    def get_queryset(self, *args, **kwargs):
        
        requested_user = self.kwargs.get("username") 
        # kwargs always gets passed on by get() method
        # in class so when using class based views
        # always use self.kwargs unless you are inside
        # get() method in a class based view

        if requested_user:                                           # same as parent=None just more Django way
            qs = Tweet.objects.filter(user__username=requested_user)#.filter(parent__isnull=True) #second filter cause we dont want to show retweets in the User's Detail View

        else:

            user_instance = self.request.user # ekhane self.request.user holo User class instance of current logged in User
            user_profile = user_instance.profile # back tracing from User class's foreign key coming to UserProfile by using related_name

            # One to one relationship so getting one data only

            #users_im_following = user_profile.following.all() # Returns all following Users Including Me
            
            users_im_following = user_profile.get_following() # method we have set up in the UserProfile class

            # filters User that is not Me cause same user ME is present in both User and Userprofile
            
            qs = Tweet.objects.filter(user__in=users_im_following) # basically SQL nested Query with the IN to compare with more than one fields
            
            qs2 = Tweet.objects.filter(user=self.request.user)
            qs = (qs | qs2).distinct()
            
        
        # sorting tweets by timestamp decending order
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
