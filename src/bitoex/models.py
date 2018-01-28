# bitoex/models.py
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Bitoex(models.Model):

    buy = models.IntegerField(
        blank=False, null=True,
        verbose_name=_('bitoex_buy')
    )
    sell = models.IntegerField(
        blank=False, null=True,
        verbose_name=_('bitoex_sell')
    )
    timestamp = models.DateTimeField(
        blank=False, null=True,
        verbose_name=_('bitoex_ts')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Bitoex')
        verbose_name_plural = _('Bitoexs')

    def __str__(self):
        return f'buy:{self.buy}, sell:{self.sell}, time:{self.timestamp}'

    def get_absolute_url(self):
        return reverse('bitoex_detail', kwargs={'pk': self.pk})