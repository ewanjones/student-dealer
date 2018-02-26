from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Business, Deal

import json


def index(request):
    return HttpResponse("This is the API endpoint")

class BusinessView(View):
    def get(self, request):
        bid = request.GET.get('', None)

        # /user/auth/<bid>
        if bid:
            business = Business.objects.get(bid)

            return JsonResponse({
                'status': 'success',
                'business': {
                    "id": business.id
                    "name": business.name
                    "area": business.area
                    "address": business.address
                    "business_type": business.type
                    "description": business.description
                    "url": business.url
                }
            })

        # /api/business/
        businesses = Business.objects.all().values()

        result = {
            'status': 'success',
            'items': []
        }

        for b in businesses:
            result = {
                "id": business.id,
                "name": business.name,
                "area": business.area,
                "address": business.address,
                "business_type": business.type,
                "description": business.description,
                "url": business.url
            }

            result['items'].append(result)

        return JsonResponse(result)



class DealView(View):
    def get(self, request):
        did = request.GET.get('', None)

        # /user/auth/<bid>
        if did:
            deal = Deal.objects.get(did)

            return JsonResponse({
                'status': 'success',
                'deal': {
                    "id": deal.id
                    "name": deal.name
                    "area": deal.area
                    "address": deal.address
                    "business_type": deal.type
                    "description": deal.description
                    "url": deal.url
                }
            })

        # /api/business/
        deals = Deal.objects.all().values()

        result = {
            'status': 'success',
            'items': []
        }

        for d in deals:
            result = {
                "id": deal.id,
                "name": deal.name,
                "area": deal.area,
                "address": deal.address,
                "business_type": deal.type,
                "description": deal.description,
                "url": deal.url
            }

            result['items'].append(result)

        return JsonResponse(result)
