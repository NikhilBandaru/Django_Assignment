from django.urls import path
from .views import *
urlpatterns = [
    path('search_movie/',search_movie),
    
]