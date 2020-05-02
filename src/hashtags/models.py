from django.db import models
from tweets.models import Tweet

class HashTag(models.Model):
    tag = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag
    
    def tag_tweets(self):
        return Tweet.objects.filter(content__icontains='#' + self.tag).order_by('-timestamp')
        
        # # + here beecause the 
        # tweet content itself has # in content
        # but the HasTag model's tag field doesn't have hastag in it
    
