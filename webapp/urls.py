from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='webapp'),
    url('welcome/', views.welcome, name='welcome')
]
