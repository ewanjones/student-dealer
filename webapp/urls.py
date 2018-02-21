from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^$', views.index, name='webapp'),
]
