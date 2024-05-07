from django.shortcuts import render, redirect


def index(request):

    return render(request, 'myapp/index.html', {'title': 'Главная страница'})


def classes(request):
    return render(request, 'myapp/classes.html', {'title': 'Классы'})

def prices(request):
    return render(request, 'myapp/prices.html', {'title': 'Цены'})

def o_nas(request):
    return render(request, 'myapp/o_nas.html', {'title': 'О нас'})

def kontact(request):
    return render(request, 'myapp/kontact.html', {'title': 'Контакты'})




