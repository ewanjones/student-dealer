from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'webapp/index.html')


def welcome(request):
    return render(request, 'webapp/welcome.html')
