from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "accounts_app/index.html")

def register(request):
    return render(request, "accounts_app/register.html")