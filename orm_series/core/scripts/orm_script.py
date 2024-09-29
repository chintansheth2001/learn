from django.contrib.auth.models import User
from core.models import Restaurant, Rating
from django.utils import timezone
from django.db  import connection
from pprint import pprint

def run():

    rating = Rating.objects.first()
    print(rating.restaurant)  
   
    pprint(connection.queries) 

    