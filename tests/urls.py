from django.urls import path

from tests import views

urlpatterns = [
    path('jquery/', views.jquery, name='tests-jquery'),
    path('ajax/', views.ajax, name='tests-ajax'),
]
