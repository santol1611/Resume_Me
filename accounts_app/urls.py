from django.contrib.auth.views import LoginView
from django.urls import path
from accounts_app import views

app_name = 'accounts_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]