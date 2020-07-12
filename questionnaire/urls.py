from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', include('questions.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
]
