from django.contrib import admin

from src.apps.hrlist.admin.models import BaseAdminModel


class CustomUserAdmin(BaseAdminModel, admin.ModelAdmin):

    list_display = ['email', 'username', 'full_name']
