from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import SoftDeletableModel

class Position(SoftDeletableModel):
    service_name = models.CharField(verbose_name=_("Сервисное название должности"), max_length=50, unique=True)
    name = models.CharField(verbose_name=_('Должность'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('Должность')
        verbose_name_plural = _('Должности')

    def __str__(self):
        return self.name
