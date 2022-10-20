from django.contrib import admin
from django.urls import path
from contact.views import Contact
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('', views.contact, name='success'),
]
