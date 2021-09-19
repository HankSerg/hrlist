from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import SoftDeletableModel

from .position import Position
from .division import Division


class Staff(SoftDeletableModel):
    """
    Сотрудник
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Сотрудник"),
        on_delete=models.PROTECT,
        related_name="staff"
    )
    position = models.ForeignKey(
        Position,
        verbose_name=_("Должность"),
        related_name="positions",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    division = models.ForeignKey(
        Division,
        verbose_name=_("Подразделение"),
        related_name="divisions",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    date_hire = models.DateField(
        verbose_name=_("Дата приёма на работу"),
        auto_now=False,
        blank=True,
        null=True,)
    salary = models.BigIntegerField(verbose_name=_("Размер заработной платы"), default=0)


    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")

    def __str__(self):
        return f"Сотрудник {self.user}"
