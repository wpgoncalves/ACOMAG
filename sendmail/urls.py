from django.urls import path
from sendmail import views

urlpatterns = [
    path('test/', views.test_send_email, name='test_send_email')
]
