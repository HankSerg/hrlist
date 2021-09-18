from django.contrib import admin

from src.apps.hrlist.admin.models import BaseAdminModel


class DivisionAdmin(BaseAdminModel, admin.ModelAdmin):

    list_display = ['name', 'slug', 'parent']
