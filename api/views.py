from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Business, Deal

import json


def index(request):
    return HttpResponse("This is the API endpoint")

class BusinessView(View):
    def get(self, request):
        businesses = Business.objects.all().values()
        result = {'status': 'success', 'items': []}

        for b in businesses:
            result['items'].append(b)

        return JsonResponse(result)


class DealView(View):
    def get(self, request):
        deals = Business.objects.all().values()
        result = {'status': 'success', 'items': []}

        for d in deals:
            result['items'].append(d)

        return JsonResponse(result)
