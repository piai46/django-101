from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luis Gustavo',
        'name2': 'Layla'
    })
