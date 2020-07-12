import uuid
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a question category (e.g. Math, Programming)')


class Question(models.Model):
    name = models.CharField(max_length=255, help_text='Enter the name of the question')
    question = models.TextField(max_length=600, help_text='Enter Question here')
    answer = models.CharField(max_length=500, help_text='Enter the answer that returns the correct result i.e a number ')
    category = models.ManyToManyField(Category, help_text='Select a category for this question')


class QuestionInstance(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help='Unique Id for this attempted question')
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    attempted_at = models.DateField(null=True, blank=True)
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

class ProgrammingQuestion(models.Model):
    # Can extend the Question model to avoid DRY
    name = models.CharField(max_length=255, help_text='Enter the name of the question')
    # For code to work properly this should be a field that respects formatting when saved 
    answer = models.CharField(max_length=500, help_text='Enter the python program that returns the correct result ')


class ProgrammingQuestionInstance(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help='Unique Id for this attempted question')
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    attempted_at = models.DateField(null=True, blank=True)
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

