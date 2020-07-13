from django.views import generic
from questions.models import Question


class QuestionListView(generic.ListView):
    # your own name for the list as a template variable
    context_object_name = 'question_list'
    queryset = Question.objects.filter(category__icontains='math')[:5]
    # Specify your own template name/location
    template_name = 'questions/question_list.html'


