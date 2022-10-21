from django.contrib import admin
from django.urls import path
from contact.views import contact
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('', views.contact, name='success'),
]
