from django.shortcuts import render
from django.http import JsonResponse

from accounts.models import User
from django.contrib.auth import authenticate, login


# not a public method!
# def get_user_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#
#     return ip

def auth_user(request, name, email):
    '''
    This is the core function - it is used here for the API and in webapp.views for a redirect endpoint
    '''
    # get user from database
    user = authenticate(email=email, name=name)
    login(request, user)

    user_object = {
        "name": user.name,
        "email": user.email
    }

    return user_object


def ajax_auth(request):
    '''
    /user/auth/
    '''

    email = request.POST.get('email')
    name = request.POST.get('name')

    user = auth_user(request, name, email)

    response = {
        "status": "success",
        "user": user
    }

    return JsonResponse(response, safe=False)
