import uuid
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=200, help_text='Enter a question category (e.g. Math, Programming, History)')

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(
        max_length=255, help_text='Enter the name of the question')
    question = models.TextField(
        max_length=600, help_text='Enter Question here')
    answer = models.CharField(
        max_length=500, help_text='Enter the solution i.e a number ')
    category = models.ManyToManyField(
        Category, help_text='Select a category for this question')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])


class QuestionInstance(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help='Unique Id for this attempted question')
    question = models.ForeignKey(
        'Question', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    attempt = models.CharField(max_length=255)

    ATTEMPT_STATUS = (
        ('p', 'Pass'),
        ('f', 'Fail'),
        ('n', 'No attempt')
    )

    status = models.CharField(
        max_length=1,
        choices=ATTEMPT_STATUS,
        blank=True,
        default='n',
        help_text='Attempt Status'
    )

    def __str__(self):
        return self.question.name
