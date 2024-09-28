import datetime
from core.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():
    print(
        Restaurant.objects.filter(
            restaurant_type=Restaurant.TypeChoices.CHINESE))
    print(connection.queries)
