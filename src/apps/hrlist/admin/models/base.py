from django.contrib import admin


class BaseAdminModel(admin.ModelAdmin):
    """
    Base Admin Model for protect delete operation.
    """
    exclude = ('is_removed', )

    def has_delete_permission(self, request, obj=None):
        return False
