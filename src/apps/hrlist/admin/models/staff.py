from django.contrib import admin

from src.apps.hrlist.admin.models import BaseAdminModel


class StaffAdmin(BaseAdminModel, admin.ModelAdmin):

    list_display = ['user', 'position', 'date_hire', 'division' ]
