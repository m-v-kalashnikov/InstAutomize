from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.settings import BASE_DIR


class CustomUser(AbstractUser):

    email = models.EmailField(verbose_name=_('Email адрес'),
                              max_length=254,
                              blank=False
                              )
    instagram_login = models.CharField(verbose_name=_('Логин от Instagram'),
                                       max_length=30,
                                       blank=False,
                                       null=True,
                                       )
    instagram_password = models.CharField(verbose_name=_('Пароль от Instagram'),
                                          max_length=256,
                                          blank=False,
                                          null=True,
                                          )
    image = models.URLField(verbose_name=_('Ссылка на аватар пользователя'),
                            max_length=512,
                            blank=True,
                            null=True,
                            )

    USERNAME_FIELD = 'username'   # e.g: "username", "email"
    EMAIL_FIELD = 'email'         # e.g: "email", "primary_email"
