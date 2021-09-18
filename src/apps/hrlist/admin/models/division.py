from django.contrib import admin

from src.apps.hrlist.admin.models import BaseAdminModel
from mptt.admin import MPTTModelAdmin


class DivisionAdmin(MPTTModelAdmin):

    list_display = ['name', 'slug', 'parent']
