from django.contrib import admin
from django.urls import path
from home import views  # Import views from the home app
from .models import Cadidate 

urlpatterns = [
    path("", views.index, name='home'),
    path("details", views.details, name='details'),
    path("cadidate", views.cadidate, name='cadidate'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'), 
]
