from django.db import models
from django.contrib.auth.models import User
from app_market.models import Order
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, verbose_name=_('balance'), max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, default=_('newbie'), verbose_name=_('status'))
    spenging_amount = models.DecimalField(default=0, verbose_name=_('spenging amount'), max_digits=20, decimal_places=2)


    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
