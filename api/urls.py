from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api'),
    path('businesses/', views.ViewBusinesses, name='businesses')
]
