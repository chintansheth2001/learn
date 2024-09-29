from core.models import Restaurant
from django.utils import timezone
from django.db  import connection

def run():
    
    print(Restaurant.objects.count())
    
    print(connection.queries) 

    