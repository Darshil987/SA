from django import forms
from django.core import validators
from .models import InputData


class AnalyzeTweets(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['topic', 'no_tweets']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Sentimental Analysis'}),
            'no_tweets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}),
        }

        labels = {
            'topic': 'Enter Topic',
            'no_tweets': 'Number of Tweets to analyze'
        }
