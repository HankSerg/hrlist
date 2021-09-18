from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import SoftDeletableModel


class Division(SoftDeletableModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    parent = models.ForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Подразделение")
        verbose_name_plural = _("Подразделения")

    def __str__(self):
        return self.name
