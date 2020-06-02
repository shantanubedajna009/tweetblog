from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):

    # extra modification as for the conetnt means overwriting the content
    # from what it already is (a charfield) adding widget like a textarea
    content = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Your Tweet"}))
    class Meta:
        model = Tweet
        fields = [
            #'user',
            'content',
        ]
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data['content']

        if content == 'abc':
            raise forms.ValidationError('Can\'t be abc')
        return content
