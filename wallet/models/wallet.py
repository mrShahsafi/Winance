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
    ("Dollar","$"),
    ("Toman","T"),

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

    def __str__(self):
        return f"wallet:{self.name}"

    @property
    def balance(self):
        income_dict = self.income_set.aggregate(Sum("price"))
        spend_dict = self.spend_set.aggregate(Sum("price"))

        income_total = income_dict['price__sum']
        spend_total = spend_dict['price__sum']

        if income_total is None and spend_total is None:
            return 0
        elif income_total is None:
            return -spend_total
        elif spend_total is None:
            return income_total

        balance = income_total - spend_total

        return balance