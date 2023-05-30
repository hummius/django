from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, verbose_name='баланс', max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, default='новичок', verbose_name='статус')
    spenging_amount = models.DecimalField(default=0, verbose_name='сумма затрат', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
