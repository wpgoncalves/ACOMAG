from django.urls import path

from customers.views import listing, register

urlpatterns = [
    path('register/', register, name='customers_register'),
    path('listing/', listing, name='customers_listing'),
]
