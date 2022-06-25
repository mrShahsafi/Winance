from graphene import Field, Argument, ID, NonNull, List, Float

from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model

from wallet.models import (
    Wallet,
    Income,
    Invest,
    Spend,
)

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class IncomeType(DjangoObjectType):
    class Meta:
        model = Income
        fields = "__all__"


class SpendType(DjangoObjectType):
    class Meta:
        model = Spend
        fields = "__all__"


class InvestmentType(DjangoObjectType):
    class Meta:
        model = Invest
        fields = "__all__"


class WalletType(DjangoObjectType):
    incomes = List(NonNull(IncomeType), required=True)
    spends = List(NonNull(SpendType), required=True)
    invests = List(NonNull(InvestmentType), required=True)
    balance = Float()
    total_spends = Float()
    remaining_cash = Float()

    class Meta:
        model = Wallet
        fields = (
            "id",
            "name",
            "description",
            "currency",
            "created_date",
            "user",
        )

    def resolve_incomes(self, info):
        return self.income_set.all()

    def resolve_spends(self, info):
        return self.spend_set.all()

    def resolve_invests(self, info):
        return self.invest_set.all()

    def resolve_balance(self, info):
        return self.balance

    def resolve_total_spends(self, info):
        return self.total_spends

    def resolve_remaining_cash(self, info):
        return self.remaining_cash


class WalletQuery:
    wallet = Field(WalletType, id=Argument(ID, required=True))

    def resolve_wallet(self, info, **kwargs):
        id = kwargs.get("id")
        try:
            return Wallet.objects.get(id=id)

        except Exception:
            return None
