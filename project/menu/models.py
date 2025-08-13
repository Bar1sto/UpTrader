from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    name = models.CharField(_('name'), max_length=100)
    named_url = models.CharField(
        _('Наименование URL'), 
        max_length=200, 
        blank=True,
    )
    url = models.CharField(
        _('URL'), 
        max_length=200, 
        blank=True,
    )
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name='Родитель'
    )
    menu_name = models.CharField(
        _('Наименование меню'), 
        max_length=100,
    )
    order = models.PositiveIntegerField(_('Позиция'), default=0)

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.named_url
        return self.url or '#'

    def is_active(self, current_path):
        return self.get_url() == current_path