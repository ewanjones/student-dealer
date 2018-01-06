from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json

from .models import Business

def index(request):
    return HttpResponse("Hello World")

def ViewBusinesses(request):
    businesses = Business.objects.all().values()
    result = {'items': []}

    for b in businesses:
        result['items'].append(b)

    return JsonResponse(result)
