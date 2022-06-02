from django.contrib import admin

from wallet.models import (
    Wallet,
    Income,
    Spend,
)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    pass


class IncomeTabularAdmin(admin.TabularInline):
    model = Income
    extra = 1


@admin.register(Spend)
class SpendAdmin(admin.ModelAdmin):
    pass


class SpendTabularAdmin(admin.TabularInline):
    model = Spend
    extra = 1


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user',
        'balance',
        "currency",
    ]

    inlines = [
        IncomeTabularAdmin,
        SpendTabularAdmin,
    ]

