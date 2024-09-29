from django.contrib.auth.models import User
from core.models import Restaurant, Rating
from django.utils import timezone
from django.db  import connection
from pprint import pprint

def run():
    
    restaurant = Restaurant.objects.last()
    restaurant.name = "Jashuben na Pizza"
    restaurant.save()
    # user = User.objects.first()
    # rating = Rating.objects.create(user=user,restaurant=restaurant, rating=3 )
    
    pprint(connection.queries) 

    