from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import ValidationError

from .models import Question, QuestionInstance
from .forms import AnswerForm


@login_required
def question_detail_view(request, question_id):
    context = {}
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        q = get_object_or_404(Question, pk=question_id)
        if form.is_valid():
            attempt = form.cleaned_data.get('attempt')
            q_instance = QuestionInstance(
                question=q, user=request.user, attempt=attempt)
            if attempt == q.answer:
                q_instance.status = 'p'
            else:
                q_instance.status = 'f'
            q_instance.save()
            context['question_instance'] = q_instance
            context['question_id'] = question_id
        return render(request, 'questions/question_result.html', context)

    else:
        context['question'] = get_object_or_404(Question, pk=question_id)
        context['attempts'] = QuestionInstance.objects.filter(
            user=request.user, question_id=question_id)
        context['question_list'] = Question.objects.all()
        context['form'] = AnswerForm()

    return render(request, 'questions/question_detail.html', context)


class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'question_list'
    queryset = Question.objects.all()
    template_name = 'questions/question_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
