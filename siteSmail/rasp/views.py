from django.shortcuts import render
from .models import Week



def raspisanie(request):
    peopless = Week.objects.order_by('time')
    return render(request, 'rasp/raspisanie.html', {'peopless': peopless})