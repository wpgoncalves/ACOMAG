from django.shortcuts import render


def jquery(request):
    return render(request, 'jquery.html')
