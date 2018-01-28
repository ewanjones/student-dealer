from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout


import json

from .models import Business, IPAddress
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("This is the API endpoint")

# not a public method!
def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


#  ----------------------
#   USER AUTHENTICATION
#  ----------------------

class Authentication(View):
    def signup(request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # create user object
        user = User.objects.create_user(email, email, None)
        user.first_name = first_name
        user.last_name = last_name

        # get users IP and store this
        user_ip = get_user_ip(request)
        ip = IPAddress(ip=ip, user=user)
        ip.save()
        # update user with ip
        user.ipaddress_set.add(ip)
        
        request.session['user_id'] = user.id

        response = {
            'status': 'success',
            'body': user
        }
        return JsonResponse(request, response)


    def login(request):
        email = request.POST.get('email')
        user = authenticate(request, email=email)
        user_ip = get_user_ip(request)

        response = {}
        if user is not None:
            login(request, user)

            # check for user ip
            user_ip_list = user.ip_set
            try:
                user_ip_list.objects.get(ip=user_ip)
            except:
                user.ip_set.add(user_ip)

            response = {
                'status': 'success',
                'email': user.email
            }
        else:
            response = {
                'status': 'failed',
                'message': 'user could not be found'
            }

            
        request.session['user_id'] = user.id

        return JsonResponse(request, response)


    def logout(request):
        try:
            del request.session['user_id']
        except KeyError:
            pass

        response = {
            'status': 'success',
            'message': 'logged in successfully'
        }

        return JsonRepsonse(request, response)



#  ----------------------
#   OTHER
#  ----------------------

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
