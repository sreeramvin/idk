from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserPageAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(UserProfile, UserPageAdmin)
