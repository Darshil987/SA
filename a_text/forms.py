from django import forms
from .models import TextInputData


class TextBodyForm(forms.ModelForm):
    class Meta:
        model = TextInputData
        fields = ['keyword', 'text_body']
        labels = {
            'text_body': '',
        }

        widgets = {
            'keyword': forms.TextInput(attrs={'class': 'form-control '}),
            'text_body': forms.TextInput(attrs={'class': 'form-control w-50'}),
        }
