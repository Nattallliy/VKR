from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('reviews/', views.AddReview.as_view(), name="add_review")

]
