from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, OwnerNotSameMixin
from django.views.generic import (DetailView,
                                  DeleteView,
                                  ListView,
                                  UpdateView,
                                  CreateView)
from django.views import View
from django.http import HttpResponseRedirect



class RetweetView(View):

    def get(self, request, pk, *args, **kwargs):
        parent_tweet = get_object_or_404(Tweet, pk=pk)
        # this raises a exception Http404 
        # directly from this point in the 
        # view and django redirects to a stock 404 page
        # if the exception is seen by django
        
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(user=request.user, parent_obj=parent_tweet)
            if new_tweet:
                return HttpResponseRedirect(new_tweet.get_absolute_url())
            else:
                return redirect("tweets:list")
        
        # user was not authenticated so no retweet
        # redirect to parent tweet detail page 
        return HttpResponseRedirect(parent_tweet.get_absolute_url())



class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    #queryset = Tweet.objects.all()
    form_class = TweetModelForm
    #fields = [
    #    'user',
    #    'content'
    #]

    template_name = "tweets/create_view.html"
    #success_url = '/tweet/create'
    login_url = reverse_lazy("home")

class TweetUpdateView(LoginRequiredMixin, OwnerNotSameMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    #success_url = '/tweet/'



class TweetDetailView(LoginRequiredMixin, OwnerNotSameMixin, DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    """def get_object(self):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk)"""
    
    def get_context_data(self, *args, **kwargs):
        context = super(TweetDetailView, self).get_context_data(*args, **kwargs)
        twt = get_object_or_404(Tweet, id=self.kwargs.get('pk'))

        # if tweet not foundd then already a 404 page is shown by django
        # which handles the Http404 Exception 
        # so we dont have to worry about checking the if tweet is valid or not

        context['is_retweet'] = Tweet.objects.is_retweet(twt)

        return context





class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"


    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        #print(self.request.GET)

        q = self.request.GET.get("q", None)
        if q:
            qs = qs.filter(
                Q(content__icontains=q) |
                Q(user__username__icontains=q)
            )
        return qs


    def get_context_data(self, *args, **kwargs):

        #getting old context
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #print(context)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweets:create")
        return context



class TweetDeleteView(LoginRequiredMixin, OwnerNotSameMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("home")
    template_name = "tweets/delete_confirm.html"























































"""def tweet_list_view(request):
    queryset = Tweet.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, "tweets/list_view.html", context=context)

def tweet_detail_view(request, id=2):
    obj = Tweet.objects.get(id=id)

    context = {
        'object': obj
    }

    return render(request, "tweets/detail_view.html", context=context)
"""
