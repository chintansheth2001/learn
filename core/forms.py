from django import forms
# from core.models import Rating, Restaurant
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import Restaurant

#class RatingForm(forms.Form):

#rating = forms.IntegerField(
#validators=[MinValueValidator(1),
#MaxValueValidator(5)])
# class Meta:
#   model = Rating
#   #fields = ('restaurant', 'user', 'rating')


class RastarantForm(forms.ModelForm):

  class Meta:
    model = Restaurant
    fields = ('name', 'restaurant_type')
