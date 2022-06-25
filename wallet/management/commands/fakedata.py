from faker import Faker
from django_seed import Seed

from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

from wallet.models import (
    Wallet,
    Income,
    Invest,
    Spend,
)

User = get_user_model()
faker = Faker()
seeder = Seed.seeder()

class Command(BaseCommand):

    def initial_setup(self,):
        # crate users
        NUMBER_OF_USERS = 10

        seeder.add_entity(User, NUMBER_OF_USERS)

        user = User.objects.create_superuser(
            username="samirsha",
            password="123456789",
        )
        user.save()
        # create Wallets
        NUMBER_OF_WALLETS = 50
        seeder.add_entity(Wallet, NUMBER_OF_WALLETS, {
            'user': lambda x: faker.random_int(min=1, max=User.objects.count()),
            'name': lambda x: faker.name(),
            'description' : lambda x: faker.name(),
        })

    def handle(self, *args, **options):
        self.initial_setup()