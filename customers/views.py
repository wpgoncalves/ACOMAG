from django.http import HttpResponse


def register(request):
    return HttpResponse(f'<h1>{request}</h1>')


def listing(request):
    return HttpResponse(f'<h1>{request}</h1>')
