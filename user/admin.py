from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAmin(BaseUserAdmin):
    fieldsets = (
        ('Credenciales', {'fields': ('username', 'password')}),
        ('Información Personal', {
         'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Redes Sociales', {'fields': ('web_site', 'twitter',)}),
    )
