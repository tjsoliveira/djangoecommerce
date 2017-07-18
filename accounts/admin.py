# coding=utf-8

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminForm

class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    form = UserAdminForm

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'email', 'is_active', 'is_staff', 'date_joined']


admin.site.register(User, UserAdmin)