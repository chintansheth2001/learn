from django import forms
from core.models import Restaurant, Rating, Sale


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('restaurant', 'user', 'rating')