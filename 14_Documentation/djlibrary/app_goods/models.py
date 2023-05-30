from django.db import models


class ItemsGroup(models.Model):
    name = models.CharField(max_length=200, default='group', verbose_name='название',)


class Item(models.Model):
    """Модель товара."""
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')
    group = models.ForeignKey(ItemsGroup, on_delete=models.CASCADE, null=True, verbose_name='группа')


