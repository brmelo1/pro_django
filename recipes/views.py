from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Bruno Melo'})

def sobre(request):
    return render(request, 'temp.html')

def cont(request):
    return render(request, 'cont.html')

# Create your views here.
