from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_index(request):
    context = {
        "title": "Главная страница",
        "text": "test",

    }    
    return render(request, 'home_app/base.html', context=context)