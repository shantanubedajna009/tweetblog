from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


class UserProfilemanager(models.Manager):

    # pretty good function to exclude myself when querying 
    
    use_for_related_fields = True  # just means use for related fields also 
    # which essentially means user.profile.all() coming from related fields here 
    # Which Means exclude That user's UserProfile 

    def all(self):
        #print(self.instance)
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass

        return qs
    
    def toggle_follow(self, user, to_toggle_user):
        user_profile, created_or_not = UserProfile.objects.get_or_create(user=user)
        
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user)
            added = True
        
        return added
    
    def is_following(self, user, followed_by_user):
        user_profile, created_or_not = UserProfile.objects.get_or_create(user=user)

        if created_or_not:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        
        return False


    def recommended(self, user, limit_to=10):
        user_profile = user.profile
        im_following = user_profile.get_following()

                                
                                # if it was a UserProfile object then to access user would be 
                                # then to access User object would be UserProfileObject.user.username for username
                                # UserProfileObject.user.id to get the OneToOne User corresponding id
                                # likewise since we are accessing the queryset inside the UserProfileObecjt itself
                                # then exclude(user__in)  means user object
                                # and the im_following is a list of User objects (cause remember accesing the following.all()
                                # from front so we get user_id from the following table)
        qs = self.get_queryset().exclude(user__in=im_following).exclude(id=user_profile.id).order_by("?")[:limit_to]
        
        #print('\n\n\n', qs.query, '\n\n\n')

        return qs



        #SELECT "accounts_userprofile"."id", "accounts_userprofile"."user_id" 
        # FROM "accounts_userprofile" 
        # WHERE (NOT
        #  ("accounts_userprofile"."user_id" IN
        #  (SELECT U0."id" FROM "auth_user" U0
        #  INNER JOIN "accounts_userprofile_following" U1
        #  ON (U0."id" = U1."user_id") WHERE
        #  (U1."userprofile_id" = 1 AND NOT
        #  (U0."username" = Hopsin01))))
        #  AND NOT ("accounts_userprofile"."id" = 1))
        #  ORDER BY RANDOM() ASC  LIMIT 10

        



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    
    
    """
    samner diye gele samner ta debe
    pichoner diye gele pichoner reference ta debe

    following is a differnt table with references 

    following
    user_id       userprofile_id

    object.profile # mane ei table e aslam onetoone rel e back trace related name diye
    
    ebar objects.profile.following eta dei hocce following table er first reference dicce user_id

    karon first diye access korchi

    objects.followed_by.all mane related name diye backtrace korchi eta dicce userprofileid karon 

    following table er pichon diye aschi tai secondary reference ta dicce userprofile_id

    """
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="followed_by")
    
    
    
    objects = UserProfilemanager() # same as  Userprofile.objects.all()
    # the objects part of it is model manager
    """
    abc = CustomModelManager()
    # this works like this UserProfile.abc.all()
    """ 




    def __str__(self):
        return str(self.following.all().count())


    """
    eta karon following diye access korle user_id ke debe first er ta 

    so otake filter korar jonno ei function ta use korte hobe

    karon eta following.all er jonno jetar mane user_id

    agger modelmanager ta ei model.all er jonno jetar mane userprofile_id

    karon eta User.objects.all ke trigger korche tai amra User model ke change korte parbo na tai
    ekhane overwrite korche ManyToManyField er all functiion take, karon ManyToManyField essentially akta table
    onekta model er moo kaj kore
    """

    def get_following(self):
        users = self.following.all() # User.objects.all().exclude(username=self.user.username)
        # this is the case because going from the front returns the first user_id reference

        return users.exclude(username=self.user)
    
    def get_follow_url(self):
        return reverse_lazy("accounts:follow", kwargs={"username": self.user.username}) 
        # self.user.username cause
        # user is oneToOne relation and we have to 
        # access the User model reference to get the username
    
    def get_absolute_url(self):
        return reverse_lazy("accounts:detail", kwargs={"username": self.user.username})