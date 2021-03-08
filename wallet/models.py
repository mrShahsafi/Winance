from django.db import models
from django.utils.text import slugify
from django.urls import reverse



class AbstractModel(models.Model):
    created_date = models.DateTimeField(
        auto_now_add = True
    )
    modified_date = models.DateTimeField(
        auto_now = True
    )
    is_deleted =  models.BooleanField(
        default=False
    )

class Wallet(AbstractModel):
    name = models.CharField(
        default='',
        max_length=256,
        verbose_name='wallet name'
    )
    income = models.FloatField(
        default=0,
        verbose_name='all of your incomes',
    )
    spent = models.FloatField(
        default=0,
        verbose_name='all of your spents',
    )
    total_money = models.FloatField(
        default=0,
        verbose_name='sum of spents and incomes',
    )
    slug = models.SlugField(
        default='wallet-slug',
        verbose_name='address of the wallet',
        editable=False,
        max_length=255,
    )

    def get_absolute_url(self):
        return reverse('wallet:detail',
                       kwargs=
                       {
                           'slug': self.slug
                       }
                       )


    def save(self, *args, **kwargs):
        name = self.name
        pk = self.pk
        self.slug = slugify( name + str(pk),
                            allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'wallet:{self.name}'


class Income(models.Model):
    description = models.CharField(
        default='',
        verbose_name='the reason of the income',
        max_length=256,
    )
    price = models.FloatField(
        default=0.0,
        verbose_name='the value of income money',
        max_length=256,
    )

class Spend(models.Model):
    description = models.CharField(
        default='',
        verbose_name='the reason of the spent',
        max_length=256,
    )
    price = models.FloatField(
        default=0.0,
        verbose_name='the value of spent money',
        max_length=256,
    )