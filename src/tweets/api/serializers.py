from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    tweet_url = serializers.SerializerMethodField('get_absolute_url')
    is_retweet = serializers.SerializerMethodField()
    class Meta:
        model = Tweet

        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'tweet_url',
            'is_retweet',
        ]
    
    def get_is_retweet(self, obj):
        if obj.parent: # if it is new tweet without retweets then obj is null
            return True
        else:
            return False

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")
    
    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
