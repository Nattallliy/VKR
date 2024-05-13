from django.shortcuts import render, redirect
from django.views import View

#from siteSmail.myapp.FORMS import ReviewForm



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


#class AddReview(View):
   # """Отзывы"""
  #  def post(self, request):
    #    form = ReviewForm(request.POST)

    #    if form.is_valid():
    #        form = form.save(commit=False)
     #       form.save()
    #    return render(request, 'myapp/index.html', {'title': 'Главная страница'})

