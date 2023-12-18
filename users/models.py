from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    user_company = models.CharField(_("Company"), max_length=100, default='')
    user_address_1 = models.CharField(_("address line 1"), max_length=100, default='')
    user_address_2 = models.CharField(_("address line 2"), max_length=100, default='')
    user_city = models.CharField(_("city"), max_length=100, default='')
    user_state = models.CharField(_("state"), max_length=100, default='')
    user_zip = models.CharField(_("zip"), max_length=100, default='')
    user_phone = models.CharField(_("phone"), max_length=100, default='')
    user_fax = models.CharField(_("fax"), max_length=100, default='')
    user_mobile = models.CharField(_("mobile"), max_length=100, default='')
    user_date_modified = models.DateTimeField(_("date modified"), auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email