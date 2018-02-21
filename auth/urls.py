from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/auth$', views.authenticate, name='auth'),
]
