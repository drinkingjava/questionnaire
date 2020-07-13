from django.contrib import admin
from .models import Question, QuestionInstance, Category

admin.site.register(Question)
admin.site.register(QuestionInstance)
admin.site.register(Category)
