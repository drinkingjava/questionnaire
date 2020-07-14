from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import ValidationError

from .models import Question, QuestionInstance
from .forms import AnswerForm


def check_answer(q_model, answer):
    return q_model.answer == answer


def question_detail_view(request, question_id):
    # Generate counts of some of the main objects
    context = {}
    status = 'f'
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
        return render(request, 'questions/question_result.html', context)

    else:
        context['question'] = get_object_or_404(Question, pk=question_id)
        context['attempts'] = QuestionInstance.objects.filter(
            user=request.user)
        print(QuestionInstance.objects.filter(user=request.user, pk=1))
        context['form'] = AnswerForm()

    return render(request, 'questions/question_detail.html', context)

    # if request.method == 'GET':
    #     question = get_object_or_404(Question, pk=question_id)
    #     context['question'] = question
    #     context['form'] = AnswerForm
    #     return render(request, 'questions/question_detail.html', context)
    # elif request.method == 'POST':
    #     form = request.POST['attempt']
    #     print(request.POST)
    #     q = Question.objects.filter(id=question_id)
    #     # if form.is_valid():
    #     #     cleaned_data = form.cleaned_data()
    #     #     print(cleaned_data)
    #     context['question'] = {
    #         'name': 'Example Question',
    #         'status': 'Passed or Failed'
    #     }
    #     return render(request, 'questions/question_result.html', context)


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


class QuestionDetailView(generic.DetailView):
    model = Question
    form_class = AnswerForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def attempt_question(request):
    return render(request, 'attempted.html')
