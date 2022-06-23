from django.contrib import admin

from wallet.models import (
    Wallet,
    Income,
    Spend,
    Invest,
)


@admin.register(Income)
class InvestAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(wallet__user=request.user)


class IncomeTabularAdmin(admin.TabularInline):
    model = Income
    extra = 1



@admin.register(Invest)
class InvestAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(wallet__user=request.user)


class InvestTabularAdmin(admin.TabularInline):
    model = Invest
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
        'balance',
        "total_spends",
        "remaining_cash",
        "currency",

    ]

    inlines = [
        IncomeTabularAdmin,
        SpendTabularAdmin,
        InvestTabularAdmin,
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(user=request.user)

