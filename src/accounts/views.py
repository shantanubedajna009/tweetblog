from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
from django.db.models.signals import post_save
from django.conf import settings

User = get_user_model()

class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/detail_view.html'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))


    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['following'] = UserProfile.objects.is_following(self.request.user, self.get_object()) # self.get_object() can be replaced with kwargs.get('username)
        return context



############ SAME VIEWS BUT FIRST ONE IS CLASS BASED SECOND ONE IS FUNCTION BASED ############################
class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)

        if request.user.is_authenticated:
            user_profile, created_or_not = UserProfile.objects.get_or_create(user=request.user)

            if toggle_user in user_profile.following.all():
                user_profile.following.remove(toggle_user)
            else:
                user_profile.following.add(toggle_user)

        return redirect('accounts:detail', username=username)



def user_follow(request, **kwargs):
    toggle_user = get_object_or_404(User, username__iexact=kwargs.get('username'))

    if request.user.is_authenticated:

        """
        #This piece of code is shifted to modelmanager in django models
        
        user_profile, created_or_not = UserProfile.objects.get_or_create(user=request.user)

        if toggle_user in user_profile.following.all():
            user_profile.following.remove(toggle_user) 
            #following returns user_id 
            #for User model cause coming from front
            # following.all() gives all User instances associated 
            # with UserProfile instances (userprofile_id)
            # likewise following.remove(user_id) # in our case toggle_user 
            # cascades the records , means deletes User instance of of id = user_id 
            # alongside also deletes that row's userprofile_id = cascade effect
            # following.add adds a new row with first row being user_id and second 
            # row implicitly populated userprofile_id
            # 
            # Like wiese followed_by.all() from User instance would have returned all 
            # userprofile_id associated with user_id and 
            # User_instance.followed_by.add()/User_instance.followed_by.remove()
            # would have added who follws me , adding and deleting them, kinda like blocking 
            # someone in facebook who followed me at some point  
        
        else:
            user_profile.following.add(toggle_user) 

        #Piece of code that was shifted ends here
        """
        
        
        if request.user.is_authenticated:
            is_added = UserProfile.objects.toggle_follow(request.user, toggle_user)
    
    # url = reverse("accounts:detail", kwargs={"username": kwargs.get("username")})
    # HttpResponseRedirect(url)
    return redirect("accounts:detail", username=kwargs.get("username"))

######################### SAME VIEW CLASS/FUNCTION ENDS HERE ###################################################################


def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:

        # erom kore chinhito kore dite hoi jokhon one to one relation e map kori
        user_profile = UserProfile.objects.get_or_create(user=instance)



### Django Signals Binding

post_save.connect(post_save_receiver, settings.AUTH_USER_MODEL)
