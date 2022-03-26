from django.urls import path

from poboxes.views import home

urlpatterns = [
    path('register/', home, name='poboxes_home'),
]
