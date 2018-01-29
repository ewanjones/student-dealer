from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='api'),
    url('business/', views.BusinessView.as_view(), name='business'),
    url('deals/', views.DealView.as_view(), name='deal'),

    # authentication
    url(r'user/login/', views.Authentication.login, name='login'),
    url(r'user/signup/', views.Authentication.signup, name='signup')
]
