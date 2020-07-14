from django.urls import path
from .views import QuestionListView, question_detail_view


urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:question_id>',
         question_detail_view, name='question-detail'),
]
