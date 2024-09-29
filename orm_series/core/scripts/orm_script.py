from django.contrib.auth.models import User
from core.models import Restaurant, Rating
from django.utils import timezone
from django.db  import connection
from pprint import pprint

def run():

    restaurant = Restaurant.objects.first()
    print(restaurant.ratings.all())

    pprint(connection.queries) 

    