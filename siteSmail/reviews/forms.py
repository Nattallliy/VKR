from django import forms

from .models import Reviews, Applications, Mails


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "text")

class ApplicationForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Applications
        fields = ("name", "phone")

class MailForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Mails
        fields = ("name", "email", "text")
