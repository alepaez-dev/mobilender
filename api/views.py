from rest_framework import generics
from django.http import JsonResponse
import os
import sys, json
from rest_framework import viewsets
from django.http import JsonResponse

# We import all models
from .models import *

# We import all serializers
from .serializers import *

# Create your views here

## Client
class ListClientAPIView(generics.ListAPIView):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer

class CreateClientAPIView(generics.CreateAPIView):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer

## Provider
class ListProviderAPIView(generics.ListAPIView):
  queryset = Provider.objects.all()
  serializer_class = ProviderSerializer

class CreateProviderAPIView(generics.CreateAPIView):
  queryset = Provider.objects.all()
  serializer_class = ProviderSerializer

## Item
class ListItemAPIView(generics.ListAPIView):
  serializer_class = ItemSerializer

  # Overiding method LIST to skip item_providers intersection and make it more readable
  def list(self, request, *args, **kwargs):
    items =Item.objects.all()
    data = self.get_serializer(items, many=True).data

    # list_providers is going to save all the providers of the item we are iterating
    list_providers = []
    for item in data:
      # We clear the list for each item
      list_providers.clear()
      # We extract items_providers
      items_providers = item.pop("items_providers")
      for provider in items_providers:
        # We get the providers id and do the query to extract all the instance
        provider_id = provider["provider"][0]
        new_provider = Provider.objects.get(id=provider_id)
        # We append it with the Json Format we prefer
        list_providers.append({"id": new_provider.id,"name": new_provider.name, "address": new_provider.address})
      item["providers"] = list_providers
    return JsonResponse({"items": data}, safe=False) 

class CreateItemAPIView(generics.CreateAPIView):
  queryset = Item.objects.all()
  serializer_class = CreateItemSerializer

## ItemProvider
class ListItemProviderAPIView(generics.ListAPIView):
  queryset = ItemProvider.objects.all()
  serializer_class = ItemProviderSerializer

## DistributionCenter
class ListDistributionCenterAPIView(generics.ListAPIView):
  queryset = DistributionCenter.objects.all()
  serializer_class = DistributionCenterSerializer

class CreateDistributionCenterAPIView(generics.CreateAPIView):
  queryset = DistributionCenter.objects.all()
  serializer_class = DistributionCenterSerializer

## AssociatedCompany
class ListAssociatedCompanyAPIView(generics.ListAPIView):
  queryset = AssociatedCompany.objects.all()
  serializer_class = AssociatedCompanySerializer

class CreateAssociatedCompanyAPIView(generics.CreateAPIView):
  queryset = AssociatedCompany.objects.all()
  serializer_class = AssociatedCompanySerializer

## Sucursal
class ListSucursalAPIView(generics.ListAPIView):
  queryset = Sucursal.objects.all()
  serializer_class = SucursalSerializer

class CreateSucursalAPIView(generics.CreateAPIView):
  queryset = Sucursal.objects.all()
  serializer_class = SucursalSerializer

## Order
class ListOrderAPIView(generics.ListAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

class CreateOrderAPIView(generics.CreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

## Order Detail
class ListOrderDetailAPIView(generics.ListAPIView):
  queryset = OrderDetail.objects.all()
  serializer_class = OrderDetailSerializer

class CreateOrderDetailAPIView(generics.CreateAPIView):
  queryset = OrderDetail.objects.all()
  serializer_class = OrderDetailSerializer
