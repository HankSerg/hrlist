from django.contrib import admin

from src.apps.hrlist.admin.models import BaseAdminModel


class PositionAdmin(BaseAdminModel, admin.ModelAdmin):

    list_display = ['name', 'service_name', ]
