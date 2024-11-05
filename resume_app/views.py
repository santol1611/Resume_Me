from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def experience(request):
    return render(request, "experience.html")