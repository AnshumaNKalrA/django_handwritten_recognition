from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "home.html")

def resultPage(request):
    return render(request, "result.html")