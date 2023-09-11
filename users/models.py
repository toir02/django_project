from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='страна')
    key = models.IntegerField(verbose_name='ключ', **NULLABLE)
    is_active = models.BooleanField(verbose_name='признак верификации', default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
