from django.shortcuts import render
from .models import Rasp



def raspisanie(request):
    peopless = Rasp.objects.all()
    return render(request, 'rasp/raspisanie.html', {'peopless': peopless})