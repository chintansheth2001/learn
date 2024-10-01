from django import forms
from core.models import Restaurant, Rating, Sale
from django.core.validators import MinValueValidator, MaxValueValidator


# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ('restaurant', 'user', 'rating')




# class RatingForm(forms.Form):
#     rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class RestaurantForm(forms.ModelForm):
    class Meta:
        model =  Restaurant
        fields = ('name', 'restaurant_type')