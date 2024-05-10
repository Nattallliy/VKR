from django.shortcuts import render
from .models import Week
from datetime import datetime, timedelta, date


def raspisanie(request):
    peopless = Week.objects.order_by('-time')
    return render(request, 'rasp/raspisanie.html', {'peopless': peopless})

def week_filter(request, pk):
    if pk == 1:
        week = Week.objects.filter(date__range=(date(2024, 5, 1), date(2024, 5, 3)))
    if pk == 2:
        week = Week.objects.filter(date__range=(date(2024, 5, 6), date(2024, 5, 10)))
    if pk == 3:
        week = Week.objects.filter(date__range=(date(2024, 5, 13), date(2024, 5, 17)))
    if pk == 4:
        week = Week.objects.filter(date__range=(date(2024, 5, 20), date(2024, 5, 25)))
    if pk == 5:
        week = Week.objects.filter(date__range=(date(2024, 5, 27), date(2024, 5, 30)))
    if pk == 6:
        week = Week.objects.filter(date__range=(date(2024, 6, 3), date(2024, 6, 7)))
    if pk == 7:
        week = Week.objects.filter(date__range=(date(2024, 6, 3), date(2024, 6, 7)))
    #if pk == 1:
     #   w = datetime.now() - timedelta(minutes=3)
     #   week = week.filter(date__gte=w)
    return render(request, 'rasp/raspisanie.html', {'week': week})