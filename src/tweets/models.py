from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from .validators import validate_content
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
import re
from hashtags.signals import parsed_hastags



class TweetModelManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent: # if parent exists for the parent
            
            og_parent = parent_obj.parent # always referenncing the root parent
            
            # so that someone just can't retweet and call the They Made The Tweet
        else: # no parent exist for the source tweet, means IT is itself the og
            og_parent = parent_obj

        # dont retweet if the user already retweeted the tweet
        qs = self.get_queryset().filter(user=user, parent=og_parent)

        # if you want to make user retweet a retweet tomorrow, just not today
        # qs = qs.filter(
        #     timestamp__year=timezone.now().year,
        #     timestamp__month=timezone.now().month,
        #     timestamp__day=timezone.now().day,
        # )

        if qs:
            # means its a retweet from the same user and did on the same day already
            return None

        
        obj = self.model( # to save inside modelmanager we use like this
            parent=og_parent,
            user=user,
            content=parent_obj.content, # content of the parent object

            # means not the source's content but immidiate parent's content
            # it can be the content parent_obj.parent.content or 
            # og_parent.content but just one unnessesary query
            # ku ku ku

        )

        obj.save()

        return obj # a modelmanager always should return something
        # ara ara

    
    def is_retweet(self, tweet):
        if tweet.parent:
            return True
        else:
            return False
    

    def toggle_like(self, user, tweet):
        if user not in tweet.liked_users.all():
            is_liked = True
            tweet.liked_users.add(user)
        else:
            is_liked = False
            tweet.liked_users.remove(user)
        
        return is_liked, tweet.liked_users.all().count()
    


class Tweet(models.Model):

    parent              = models.ForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content             = models.CharField(max_length=140, validators=[validate_content])
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    liked_users         = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_tweets")
    isReply             = models.BooleanField(verbose_name="is a reply ?", default=False)

    objects = TweetModelManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweets:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-timestamp"]


"""     def clean(self, *args, **kwargs):
        content = self.content

        if content == 'abc':
            raise ValidationError('Nigga can\'t be abc')
        return super(Tweet, self).clean(*args, **kwargs) """





def tweet_save_listener(sender, instance, *args, **kwargs):
    
    #pre save is pretty cool whatever we chnge contentto be it will be saved as that
    #instance.content = "DIO BRANDOOOOOOOOOO"
    

    user_regex = r'@(?P<username>>[\w.@+-]+)'
    hashtag_regex = r'#(?P<hashtag>[\w\d-]+)'

    usrnms = re.findall(user_regex, instance.content)
    #print(usrnms)

    htgs = re.findall(hashtag_regex, instance.content)
    #print(htgs)
    parsed_hastags.send(sender=instance.__class__, hashtag_list=htgs) 
    # sender is always the 
    # blueprint class without
    # the data associated with it
    

pre_save.connect(tweet_save_listener, Tweet)
# pretty straightforward 
# just mapping with the model we want this post_save listener to work on 