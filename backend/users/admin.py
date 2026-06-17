from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_active'
    )

    list_filter = (
        'role',
        'is_active'
    )

    ordering = ('id',)

    fieldsets = UserAdmin.fieldsets + (
        (
            'Información adicional',
            {
                'fields': (
                    'phone',
                    'role',
                )
            }
        ),
    )