from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('reviews/', views.AddReview.as_view(), name="add_review"),
    path('applications/', views.AddApplication.as_view(), name="add_application"),
    path('mails/', views.AddMail.as_view(), name="add_mail")
]
