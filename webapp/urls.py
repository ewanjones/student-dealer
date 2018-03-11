from django.conf.urls import url

from . import views

app_name='webapp'

urlpatterns = [
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^deals/$', views.deals, name='deals'),
    url(r'^businesses/$', views.businesses, name='businesses'),
    url(r'^$', views.index, name='index'),
]
