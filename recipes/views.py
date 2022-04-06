from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luis Gustavo',
        'name2': 'Layla'
    })


def sobre_view(request):
    return HttpResponse('SOBRE 1')


def contato_view(request):
    return HttpResponse('CONTATO 1')
