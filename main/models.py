from django.db import models


class Transport(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    description = models.CharField(max_length=30, verbose_name='описание')
    can_move = models.BooleanField(verbose_name='на ходу')

    class Meta:
        ordering = ('name', '-can_move')
        verbose_name = 'транспорт'
        verbose_name_plural = 'транспорт'
