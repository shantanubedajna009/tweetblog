from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:

            
            # this part happens auto if we dont define a mixin
            # this is used here cause we need to check if the user is authenticated
            form.instance.user = self.request.user

            # returning it to the same pipleine it came from
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User Must Be Logged In'])
            return self.form_invalid(form)

class OwnerNotSameMixin(object):
    def form_valid(self, form):

        # dont need to set user here its already set with the FormUserNeededMixin
        # and also dont need to set user cause we are not creating a tweet
        # so the tweet is already associated with a user
        if form.instance.user == self.request.user:
            return super(OwnerNotSameMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['Owner is not the same'])
            return self.form_invalid(form)
