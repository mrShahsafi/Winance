from django.db.models import (
    CharField,
    SlugField,
    ForeignKey,
    CASCADE,
)
from django.db.models import Sum
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from django.urls import reverse

from .base import AbstractModel

User = get_user_model()

CURRENCIES = (
    ("Dollar", "$"),
    ("Toman", "T"),
)


class Wallet(AbstractModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
    )

    currency = CharField(
        max_length=6,
        choices=CURRENCIES,
        default="T",
    )

    slug = SlugField(
        default="wallet-slug",
        verbose_name="address of the wallet",
        editable=False,
        max_length=255,
    )

    def get_absolute_url(self):
        return reverse("wallet:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        name = self.name
        pk = self.pk
        self.slug = slugify(f"{name}-{pk}", allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def balance(self):
        # this will calculate the balance of the wallet
        # and will not calculate the investmnet money
        # because investment money will not spent
        # it remain in wallet but as INVESTMENT.

        income_dict = self.income_set.aggregate(Sum("price"))
        spend_dict = self.spend_set.aggregate(Sum("price"))

        income_total = income_dict["price__sum"]
        spend_total = spend_dict["price__sum"]

        if income_total is None and spend_total is None:
            return 0
        elif income_total is None:
            return -spend_total
        elif spend_total is None:
            return income_total

        balance = income_total - spend_total

        return balance

    def __str__(self):
        return f"wallet:{self.name}"

    @property
    def total_spends(self):
        spend_dict = self.spend_set.aggregate(Sum("price"))

        spend_total = spend_dict["price__sum"]
        if spend_total is None:
            spend_total = 0.0
        return spend_total

    @property
    def remaining_cash(self):
        # this function will calculate the current cash money
        # that you can spend or store

        invest_dict = self.invest_set.aggregate(Sum("price"))

        invest_total = invest_dict["price__sum"]
        if invest_total is None:
            invest_total = 0.0
        balance = self.balance
        if balance is None:
            balance = 0.0
        remaining_cash = balance - invest_total
        return remaining_cash

    def __str__(self):
        return f"wallet:{self.name}"
