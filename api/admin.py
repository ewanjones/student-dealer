from django.contrib import admin

from .models import Business, Deal, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Business)
admin.site.register(Deal)
admin.site.register(User, UserAdmin)
