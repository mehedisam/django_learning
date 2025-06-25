from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api import views

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',views.registrationView,name='register'),
]
