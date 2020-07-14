from django import forms
from django.contrib.auth.models import User
from .models import QuestionInstance


class AnswerForm(forms.ModelForm):

    class Meta:
        model = QuestionInstance
        fields = ['attempt']

    widget = {
        'attempt': forms.TextInput(attrs={'class': 'form-control'})
    }
