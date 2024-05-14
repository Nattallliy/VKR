from django.shortcuts import render
from django.views import View

from .forms import ReviewForm, ApplicationForm, MailForm

from .models import Reviews


# Create your views here.
def reviews(request):
    p = Reviews.objects.all()
    return render(request, 'reviews/reviews.html', {'p': p})

class AddReview(View):
    """Отзывы"""
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
         #   form = form.save(commit=False)
           form.save()
        return render(request, 'reviews/reviews.html')


class AddApplication(View):
    """Заявка"""
    def post(self, request):
        form = ApplicationForm(request.POST)

        if form.is_valid():
         #   form = form.save(commit=False)
           form.save()
        return render(request, 'myapp/prices.html')

class AddMail(View):
    """Заявка"""
    def post(self, request):
        form = MailForm(request.POST)

        if form.is_valid():
         #   form = form.save(commit=False)
           form.save()
        return render(request, 'myapp/index.html')