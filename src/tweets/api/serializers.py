from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince
from django.urls import reverse, reverse_lazy

class ParentTweetModelSerializer(serializers.ModelSerializer):

    parent_id = serializers.CharField(write_only=True, required=False)

    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    tweet_url = serializers.SerializerMethodField('get_absolute_url')
    retweet_url = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet

        fields = [
            'parent_id',
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'tweet_url',
            'retweet_url',
            'likes_count',
            'is_liked_by_user',
            'isReply',
        ]

        #read_only_fields = ['isReply']
    
    def get_is_liked_by_user(self, obj):


        try:

            # to access an extra context (that we inject)
            # we need to process it from serializers
            # all request.user or request in general related processing
            # is done in Views and Views only
            # if we need to process something request related
            # in serializers, we need to pass it as context to be able
            # access in serializers, cause By default serializers only create 
            # contexts based on the model fields
            request = self.context.get('requested_user')
            user = request.user

            #print('\n\n\n', user, '\n\n\n')

            if user.is_authenticated:
                if user in obj.liked_users.all():
                    return True
        except:
            pass

        return False

    def get_likes_count(self, obj):
        return obj.liked_users.all().count()
    

    def get_retweet_url(self, obj):
        return reverse("tweet-api:retweet", kwargs={"pk": obj.pk})

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")
    
    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()




class TweetModelSerializer(serializers.ModelSerializer):

    parent_id = serializers.CharField(write_only=True, required=False)

    user = UserDisplaySerializer(read_only=True)
    # this is same as the ParentTweetSerializer
    # only difference is that the UserDisplaySerializer
    # is in another file in the accounts app thats all

    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    tweet_url = serializers.SerializerMethodField('get_absolute_url')
    is_retweet = serializers.SerializerMethodField()
    retweet_url = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()
    

    # make other serializers read_only if you dont want to populate (ovverride) the referencce 
    # with foreign key from this model, like here we dont want to override the parent instance
    # cause we want to see the parent attached to it
    # if that is the case make read_only=True which makes same crud operation possible from the 
    # rest api view and read the referenced parent/user data  
    parent = ParentTweetModelSerializer(read_only=True)  # this will be equal to the model
    # since the model has the parent self as foreign key because of that
    # if we reference it here it will reference the parent auto if present
    # otherwise null, adding fields which are as foreign key in serializers
    # are not nessesary but it can be added anyways

    class Meta:
        model = Tweet

        fields = [
            'parent_id',
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'tweet_url',
            'parent',
            'is_retweet',
            'retweet_url',
            'likes_count',
            'is_liked_by_user',
            'isReply',
        ]

        #read_only_fields = ['isReply']
    
    def get_is_liked_by_user(self, obj):


        try:

            # to access an extra context (that we inject)
            # we need to process it from serializers
            # all request.user or request in general related processing
            # is done in Views and Views only
            # if we need to process something request related
            # in serializers, we need to pass it as context to be able
            # access in serializers, cause By default serializers only create 
            # contexts based on the model fields
            request = self.context.get('requested_user')
            user = request.user

            #print('\n\n\n', user, '\n\n\n')

            if user.is_authenticated:
                if user in obj.liked_users.all():
                    return True
        except:
            pass

        return False

    def get_likes_count(self, obj):
        return obj.liked_users.all().count()
    
    def get_is_retweet(self, obj):
        if obj.parent: # if it is new tweet without retweets then obj is null
            return True
        else:
            return False
    def get_retweet_url(self, obj):
        return reverse("tweet-api:retweet", kwargs={"pk": obj.pk})

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")
    
    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
