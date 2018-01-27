from django.contrib import admin

from .models import Business, Deal
from django.contrib.auth.models import User


admin.site.register(Business)
admin.site.register(Deal)
