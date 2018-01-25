from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api'),
    path('business/', views.BusinessView.as_view(), name='business'),
    path('deals/', views.DealView.as_view(), name='deal'),
    path('user/', views.Signin, name='user'),
]
