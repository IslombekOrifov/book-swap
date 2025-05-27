from django.contrib import admin
from .models import Exchange


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('book', 'from_user', 'to_user', 'status', 'created_at', 'is_completed')
    list_filter = ('status', 'is_completed')
    search_fields = ('book__title', 'from_user__username', 'to_user__username')