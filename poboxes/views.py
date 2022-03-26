from django.http import HttpResponse


def home(request):
    return HttpResponse(f'<h1>{request}</h1>')
