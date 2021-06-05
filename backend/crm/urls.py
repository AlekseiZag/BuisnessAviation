from django.urls import path
from crm import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('fleet', views.fleet, name='fleet'),
    path('contacts', views.contacts, name='contacts'),
    path('card', views.card, name='card'),
    path('thanks_call', views.thanks_page_call, name='thanks_call'),
    path('thanks_booking', views.thanks_page_booking, name='thanks_booking'),
]
