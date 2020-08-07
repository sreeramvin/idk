from django.contrib import admin
from .models import UserProfile
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class UserPageAdmin(admin.ModelAdmin):
    search_fields = ['Name']

class UserExportAdmin(ImportExportModelAdmin):
    pass

class UserPageExportAdmin(UserPageAdmin, UserExportAdmin):
    pass

admin.site.register(UserProfile, UserPageExportAdmin)
