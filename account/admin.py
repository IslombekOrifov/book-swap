from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'reputation', 'books_shared')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'middle_name', 'email', 'photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('BookSwap Stats', {'fields': ('reputation', 'books_shared')}),
    )