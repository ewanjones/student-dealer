from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'webapp/index.html')


def welcome(request):
    return render(request, 'webapp/welcome.html')

def deals(request):
    return render(request, 'webapp/deals.html')

def businesses(request):
    return render(request, 'webapp/businesses.html')
