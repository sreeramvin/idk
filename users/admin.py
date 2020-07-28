from django.contrib import admin
from .models import Users
# Register your models here.

class UserPageAdmin(admin.ModelAdmin):
    search_fields=['name']
    
admin.site.register(Users,UserPageAdmin)