from django.contrib import admin

from wallet.models import (
    Wallet,
    Income,
    Spend,
)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(wallet__user=request.user)


class IncomeTabularAdmin(admin.TabularInline):
    model = Income
    extra = 1


@admin.register(Spend)
class SpendAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(wallet__user=request.user)


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

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(user=request.user)

