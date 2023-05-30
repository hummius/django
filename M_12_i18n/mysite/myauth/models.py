from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def profile_avatar_directory_path(instance: 'Profile.user', filename: str) -> str:
    return 'profiles/profile_{pk}/avatar/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    bio = models.TextField(max_length=500, blank=True, verbose_name=_('bio'))
    agreement_accepted = models.BooleanField(default=False, verbose_name=_('agreement_accepted'))
    avatar = models.ImageField(null=True, blank=True,
                               upload_to=profile_avatar_directory_path, verbose_name=_('avatar'))
    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')
