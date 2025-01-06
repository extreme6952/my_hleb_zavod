from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdminModelAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['created','updated']


@admin.register(Profile_Company)
class ProfileCompanyModelAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['created','updated',]