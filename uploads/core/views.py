from django.shortcuts import render
from django.core.files.storage import FileSystemStorage




def home(request):
    return render(request, 'home.html')


def bosak(request):
    return render(request, 'bosak.html')

def biedron(request):
    return render(request, 'biedron.html')

def duda(request):
    return render(request, 'duda.html')

def holownia(request):
    return render(request, 'holownia.html')


