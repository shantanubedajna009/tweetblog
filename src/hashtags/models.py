from django.db import models
from tweets.models import Tweet
from hashtags.signals import parsed_hastags


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

    

def parsed_hashtag_receiver(sender, hashtag_list, *args, **kwargs):
    
    # iterating through list of hashtags sent from the tweet post save model
    # and parsing each one of them , if not present in database then create it
    # so when we click on a hashtag in the frontend we dont get a 404

    for hstg in hashtag_list:
        obj = HashTag.objects.get_or_create(tag=hstg)
    



# it is connected , but gets fired from tweetmodel pre save 
# means whenever the .send is called in the parsed_hastags receiver
# it invokes the signal parsed_hastags
# it calls the parsed hastag receiver method which is connected to
# parsed_hashtag signal
# we can then do whatever we want with it
parsed_hastags.connect(parsed_hashtag_receiver)

    
