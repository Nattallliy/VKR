from django.urls import path
from . import views

urlpatterns = [
    path('', views.raspisanie, name='raspisanie'),
    path('filter/<int:pk>', views.week_filter, name='week_filter'),


]
