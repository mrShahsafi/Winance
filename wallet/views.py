from django.shortcuts import render
from django.views.generic import (View,
                            )
from django.http import HttpResponse
from .models import Wallet
from .forms import WalletCreateForm

class WalletHome(View):
    def get(self,request):
        return HttpResponse('Welcome')

class WalletLists(View):
    def get(self,request):
        query = Wallet.objects.all()
        return HttpResponse(f'{query}')

class WalletDetail(View):
    def get(self,request,slug):
        return HttpResponse (f'Detail{slug}')
