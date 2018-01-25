from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

import json

from .models import Business



def index(request):
    return HttpResponse("Hello World")


def Signin(request):
    email = request.GET.get['email']


class BusinessView(View):
    def get(self, request):
        businesses = Business.objects.all().values()
        result = {'items': []}

        for b in businesses:
            result['items'].append(b)

        return JsonResponse(result)


class DealView(View):
    def get(self, request):
        deals = Business.objects.all().values()
        result = {'items': []}

        for d in deals:
            result['items'].append(d)

        return JsonResponse(result)
