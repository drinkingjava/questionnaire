from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('', include('questions.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', include('accounts.urls')),

]
