from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        CLIENT = 'CLIENT', 'Cliente'
        DELIVERY = 'DELIVERY', 'Repartidor'

    first_name = models.CharField(
        max_length=100,
        verbose_name='Nombres'
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='Apellidos'
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Teléfono'
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"