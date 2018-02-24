from django.shortcuts import render
from django.http import JsonResponse

from accounts.models import User
from django.contrib.auth import authenticate


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


def auth_user(request):
    email = request.POST.get('email')
    name = request.POST.get('name')

    # get user object
    user = authenticate(email=email, name=name)

    user_object = {
        'name': user.name,
        'email': user.email
    }

    response = {
        'status': 'success',
        'body': user_object
    }

    return JsonResponse(request, response)
