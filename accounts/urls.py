from django.contrib import admin
from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.sign_up, name='sign_up')
]
