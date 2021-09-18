from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import SoftDeletableModel
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    """
    Custom user model for all users.
    """
    middle_name = models.CharField(verbose_name=_('Отчество'), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        permissions = ()

    @property
    def full_name(self) -> str:
        """
        Сборка ФИО.
        :return: ФИО
        """
        full_name = '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)
        return full_name.strip()

    def __str__(self):
        return f'{self.full_name} {self.email}'
