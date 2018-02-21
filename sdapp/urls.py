from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include('api.urls')),
    url('user/', include('accounts.urls')),
    url('', include('webapp.urls'))
]
