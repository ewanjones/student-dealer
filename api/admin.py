from django.contrib import admin

from .models import User, Business, Deal

admin.site.register(User)
admin.site.register(Business)
admin.site.register(Deal)
