from django.urls import path
from . import views

urlpatterns = [
    path('', views.raspisanie, name='raspisanie'),

]
