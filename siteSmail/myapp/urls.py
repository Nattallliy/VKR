from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('prices/', views.prices, name='prices'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('kontact/', views.kontact, name='kontact'),





]
urlpatterns += staticfiles_urlpatterns()


