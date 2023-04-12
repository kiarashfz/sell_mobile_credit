from django.contrib import admin

from sellers.models import Seller, SellerCreditOrder


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'credit', 'is_calculations_correct', 'get_calculation_error_amount', 'total_charged_credit',
        'total_buy_amount', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'credit')


@admin.register(SellerCreditOrder)
class SellerCreditOrderAdmin(admin.ModelAdmin):
    list_display = ('seller', 'amount', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('seller__name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
