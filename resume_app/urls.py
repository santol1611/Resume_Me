from django.urls import path
from resume_app import views

app_name = 'resume_app'

urlpatterns = [
    path('', views.index, name='index'),
   
]