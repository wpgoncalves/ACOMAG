from django.shortcuts import render


def jquery(request):
    return render(request, 'jquery.html')


def ajax(request):
    return render(request, 'ajax.html')
