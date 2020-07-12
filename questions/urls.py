from django.urls import path
from .views import question_view

urlpatterns = [
    path('', question_view  ,name='questions_view')
]