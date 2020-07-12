from django import forms
from django.contrib.auth.models import User
from .models import QuestionInstance

class AnswerForm(forms.ModelForm):
    # answer = forms.CharField(max_length=widget=forms.TextInput)

    class Meta:
        model = QuestionInstance
        fields = []