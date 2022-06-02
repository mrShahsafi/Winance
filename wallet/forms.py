from django.forms import ModelForm

# from django.forms import Form
from wallet.models.wallet import Wallet


class WalletCreateForm(ModelForm):
    class Meta:
        model = Wallet
        fields = [
            "name",
        ]
