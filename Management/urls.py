from django.urls import path
from .views import *


urlpatterns = [
    path("",Index),
    path("hotel-api/",get_api)
]
