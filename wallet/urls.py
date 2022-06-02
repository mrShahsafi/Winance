from django.urls import path, include
from .views import (
    WalletHome,
    WalletLists,
    WalletDetail,
    WalletCreate,
)

app_name = "wallet"

urlpatterns = [
    path("home/", WalletHome.as_view(), name="home"),
    path("list/", WalletLists.as_view(), name="list"),
    path("<slug>/", WalletDetail.as_view(), name="detail"),
    path("create/", WalletCreate.as_view(), name="create"),
]
