
from rest_framework import serializers
import os
from django.contrib.postgres.fields import ArrayField

# In this file, we allow data as querysets and models instances and we render them into JSON data.
# Here we also validate and control de output(logic) of the responses.
# Serializers define the API representation.


# We import all the models
from .models import *

class ClientSerializer(serializers.ModelSerializer):
  """Client"""
  class Meta:
    model = Client
    fields = [
      "name",
      "key",
      "photography",
      "address"
    ]

class ProviderSerializer(serializers.ModelSerializer):
  """Provider"""
  class Meta:
    model = Provider
    fields = [
      "id",
      "name",
      "address"
    ]

class ItemProviderSimpleSerializer(serializers.ModelSerializer):
  """ItemProvider"""
  
  class Meta:
    model = ItemProvider
    fields = ["provider"]

class ItemSerializer(serializers.ModelSerializer):
  """Item"""
  items_providers = ItemProviderSimpleSerializer(many=True)

  class Meta:
    model = Item
    fields = [
      "id",
      "description",
      "price",
      "items_providers"
    ]

class ItemProviderSerializer(serializers.ModelSerializer):
  """ItemProvider"""
  provider = ProviderSerializer(many=True)
  item = ItemSerializer()
  class Meta:
    model = ItemProvider
    fields = [
      "provider",
      "item"
    ]

class ItemProviderSingleArraySerializer(serializers.ModelSerializer):
  """ItemProvider"""
  # We make it an array field so we can POST all providers IDs in one single array and not multiple objects
  provider = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
  class Meta:
    model = ItemProvider
    fields = [
      "provider",
    ]

class CreateItemSerializer(serializers.ModelSerializer):
  """Item"""
  items_providers = ItemProviderSingleArraySerializer(many=True)
  class Meta:
    model = Item
    fields = [
      "description",
      "price",
      "items_providers"
    ]

  def create(self, validated_data):
    items_providers = validated_data.pop("items_providers")
    providers = items_providers[0].pop("provider")
    
    # We create the item
    item = Item.objects.create(**validated_data)
    item.save()
    
    # For every provider we will do an item_provider with the same item and all the providers
    for provider in providers:
      item_provider = ItemProvider.objects.create(item=item)
      item_provider.save()
      item_provider.provider.add(provider)
    
    return item

# Type of centers(Order)
class DistributionCenterSerializer(serializers.ModelSerializer):
  """DistributionCenter"""
  class Meta:
    model: DistributionCenter
    fields = "__all__"

class AssociatedCompanySerializer(serializers.ModelSerializer):
  """DistributionCenter"""
  class Meta:
    model: AssociatedCompany
    fields = "__all__"

class SucursalSerializer(serializers.ModelSerializer):
  """DistributionCenter"""
  class Meta:
    model: Sucursal
    fields = "__all__"

# Orders
class OrderSerializer(serializers.ModelSerializer):
  """DistributionCenter"""
  class Meta:
    model: Order
    fields = "__all__"