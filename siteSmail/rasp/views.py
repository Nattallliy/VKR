from django.shortcuts import render
from .models import Articles



def raspisanie(request):
   # rasp = Articles.objects.all()
    return render(request, 'rasp/raspisanie.html', {'title': 'Расписание'})#, {'rasp': rasp})

