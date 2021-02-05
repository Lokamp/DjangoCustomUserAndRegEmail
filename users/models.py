from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import CustomUserManager


class DefaultUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        primary_key=True
    )
    email = models.EmailField(
        verbose_name="Email",
        max_length=60,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_employment = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class CompanyUser(models.Model):
    user = models.OneToOneField(
        DefaultUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='company'
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=30
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=30
    )
    date_joined = models.DateField(
        verbose_name="Дата регистрации",
        auto_now_add=True
    )
    time_joined = models.TimeField(
        verbose_name="Время регистрации",
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user} {self.first_name}'
