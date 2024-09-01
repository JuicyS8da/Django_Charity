from django.urls import path
from .views import donate_view, success_view, cancel_view

urlpatterns = [
    path('donate/', donate_view, name='donate'),
    path('donate/success/', success_view, name='success'),
    path('donate/cancel/', cancel_view, name='cancel'),
]