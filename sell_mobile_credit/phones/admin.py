from django.contrib import admin

from phones.models import SimCard, SimCreditOrder


@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    list_display = ('number', 'credit', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('number',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'credit')


@admin.register(SimCreditOrder)
class SimCreditOrderAdmin(admin.ModelAdmin):
    list_display = ('sim_card', 'seller', 'amount', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('sim_card__number', 'seller__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
