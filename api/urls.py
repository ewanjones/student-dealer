from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api'),
    path('business/', views.BusinessView.as_view(), name='business'),
    path('deals/', views.DealView.as_view(), name='deal'),

    # authentication
    path(r'user/login/', views.Authentication.login, name='login'),
    path(r'user/signup/', views.Authentication.signup, name='signup')
]
