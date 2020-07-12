from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import QuestionInstance

@login_required
def question_view(request):
    
    return render(request, 'questions/questions.html')

def attempt_question(request):
    return render(request, 'attempted.html')

