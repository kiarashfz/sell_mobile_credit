from django.contrib import admin

from sellers.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'credit', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'credit')
