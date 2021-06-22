from rest_framework import generics
from django.http import JsonResponse
import os
import sys, json
from rest_framework import viewsets

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
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class CreateItemAPIView(generics.CreateAPIView):
  queryset = Item.objects.all()
  serializer_class = CreateItemSerializer

## ItemProvider
class ListItemProviderAPIView(generics.ListAPIView):
  queryset = ItemProvider.objects.all()
  serializer_class = ItemProviderSerializerr

class CreateItemProviderAPIView(generics.CreateAPIView):
  queryset = ItemProvider.objects.all()
  serializer_class = ItemProviderSerializer