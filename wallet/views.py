from django.shortcuts import render
from django.views.generic import (
    View,
)
from django.http import HttpResponse
from wallet.models.wallet import Wallet
from .forms import WalletCreateForm


class WalletHome(View):
    def get(self, request):
        return render(request, "wallet/home.html")


class WalletLists(View):
    def get(self, request):
        query = Wallet.objects.all()
        content = {"WalletList": query}
        return render(request, "wallet/list.html", content)


class WalletDetail(View):
    def get(self, request, slug):
        query = Wallet.objects.filter(slug=slug)
        content = {"WalletDetail": query}
        return render(request, "wallet/detail.html", content)

    def post(self, request, slug):
        query = Wallet.objects.filter(slug=slug)
        for object in query:
            income = object.income
            spent = object.spent
        if "income" in request.POST:
            print("return" + str(self.request.POST.get("income")))
            income += float(self.request.GET.get("income"))
            object.save()
            return HttpResponse("updated")
        elif "spent" in request.POST:
            spent += str(self.request.POST.get("spent"))
            object.save()
            return HttpResponse("updated")


class WalletCreate(View):
    def get(self, request):
        form = WalletCreateForm()
        return render(request, "wallet/create.html", form)

    def post(self, request):
        form = WalletCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form saved")
