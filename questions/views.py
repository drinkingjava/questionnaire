from django.views import generic
from questions.models import Question
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Question, QuestionInstance
from .forms import AnswerForm


def question_detail_view(request, question_id):
    # Generate counts of some of the main objects
    context = {}
    if request.method == 'GET':
        question = get_object_or_404(Question, pk=question_id)
        context['question'] = question
        context['form'] = AnswerForm
        return render(request, 'questions/question_detail.html', context)


def attempt_question(request, question_id):
    context = []
    if request.method == 'POST':
        form = request.POST['attempt']
        print(form)
        q = Question.objects.filter(id=question_id)
        context['question'] = {
            'name': 'Example Question',
            'status': 'Passed or Failed'
        }
        return render(request, 'questions/question_result.html', context)


class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'question_list'
    queryset = Question.objects.all()
    # Specify your own template name/location
    template_name = 'questions/question_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
class QuestionDetailView(generic.DetailView):
    model = Question
    form_class = AnswerForm


def attempt_question(request):
    return render(request, 'attempted.html')
