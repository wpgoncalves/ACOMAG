from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.views.generic import RedirectView


def home(request):
    return render(request, 'base/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', RedirectView.as_view(url='admin/'), name='admin'),
    path("poboxes/", include('poboxes.urls')),
    path("customers/", include('customers.urls')),
    path('', home, name='home'),
    path('email/', include('sendmail.urls')),
    path('tests/', include('tests.urls')),
]
