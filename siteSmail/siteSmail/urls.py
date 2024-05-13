
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('raspisanie/', include('rasp.urls')),
    path('reviews/', include('reviews.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Добавили новый маршрут
]


LOGIN_REDIRECT_URL = 'home'