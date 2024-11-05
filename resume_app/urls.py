from django.urls import path
from resume_app import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('experience', views.experience),
    path('projects', views.projects),
]