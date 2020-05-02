from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from .validators import validate_content
from django.contrib.auth import get_user_model



class TweetModelManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent: # if parent exists for the parent
            
            og_parent = parent_obj.parent # always referenncing the root parent
            
            # so that someone just can't retweet and call the They Made The Tweet
        else: # no parent exist for the source tweet, means IT is itself the og
            og_parent = parent_obj
        
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
    

class Tweet(models.Model):

    parent              = models.ForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content             = models.CharField(max_length=140, validators=[validate_content])
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)

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
