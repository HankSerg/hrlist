from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models as admin_models

from src.apps.hrlist import models

admin.site.register(models.CustomUser, admin_models.CustomUserAdmin)
admin.site.register(models.Division, MPTTModelAdmin)
