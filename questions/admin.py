from django.contrib import admin

from .models import Question, QuestionInstance

admin.site.register(Question)
admin.site.register(QuestionInstance)
