from django.shortcuts import render
from .models import Peoples



def raspisanie(request):
    peopless = Peoples.objects.all()
    return render(request, 'rasp/raspisanie.html', {'peopless': peopless})
