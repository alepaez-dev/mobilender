
from rest_framework import serializers
import os
from django.contrib.postgres.fields import ArrayField
from rest_framework.exceptions import ValidationError, ParseError

# In this file, we allow data as querysets and models instances and we render them into JSON data.
# Here we also validate and control de output(logic) of the responses.
# Serializers define the API representation.


# We import all the models
from .models import *

# Client
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


# Provider
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

class GetItemSerializer(serializers.ModelSerializer):
  """Item"""

  class Meta:
    model = Item
    fields = [
      "description",
      "price",
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
    model = DistributionCenter
    fields = [
      "warehouse"
    ]

class AssociatedCompanySerializer(serializers.ModelSerializer):
  """DistributionCenter"""
  class Meta:
    model = AssociatedCompany
    fields = "__all__"

class SucursalSerializer(serializers.ModelSerializer):
  """DistributionCenter"""
  class Meta:
    model = Sucursal
    fields = "__all__"


# Order Detail
class OrderDetailSerializer(serializers.ModelSerializer):
  """Order Detail"""
  class Meta:
    model = OrderDetail
    fields = [
      "quantity",
      "item"
    ]

class GetOrderDetailItemSerializer(serializers.ModelSerializer):
  """Order Detail"""
  item = GetItemSerializer()
  class Meta:
    model = OrderDetail
    fields = [
      "quantity",
      "item"
    ]

# Order with more specify details of all foreign keys serializers
class GetOrderSerializer(serializers.ModelSerializer):
  """Order"""
  distribution_center = DistributionCenterSerializer()
  associated_company = AssociatedCompanySerializer()
  sucursal = SucursalSerializer()
  client = ClientSerializer()
  orders_details = GetOrderDetailItemSerializer(many=True)
  
  class Meta:
    model = Order
    fields = [
      "id",
      "client",
      "distribution_center",
      "associated_company",
      "sucursal",
      "date_created",
      "date_stocked",
      "is_urgent",
      "orders_details"
    ]

# Order
class OrderSerializer(serializers.ModelSerializer):
  """Order"""
  orders_details = OrderDetailSerializer(many=True)

  class Meta:
    model = Order
    fields = [
      "id",
      "client",
      "distribution_center",
      "associated_company",
      "sucursal",
      "date_created",
      "date_stocked",
      "is_urgent",
      "orders_details"
    ]
  def create(self, validated_data):
    # We create de order first
    orders_details = validated_data.pop("orders_details")
    order = Order.objects.create(**validated_data)
    # THEN we create the OrderDetail and we pass it our recent created order as a parameter
    order_detail = OrderDetail.objects.create(order=order, **orders_details[0])
    return order

  def update(self, instance, validated_data):
    # First we validate the date_stocked is not before the date_created of the order
    if validated_data["date_stocked"] < instance.date_created:
      raise ValidationError("The entered date_stocked has to be after the date_created")
    
    # We check where is going to be the order
    # Wherever it is, we check the other 2 as None. EX: if it's distribution center, we check associated company and sucursal as None
    if validated_data.get('distribution_center'):
      validated_data["associated_company"] = None
      validated_data["sucursal"] = None
    elif validated_data.get('associated_company'):
      validated_data["distribution_center"] = None
      validated_data["sucursal"] = None
    elif validated_data.get('sucursal'):
      validated_data["distribution_center"] = None
      validated_data["associated_company"] = None
    return super().update(instance, validated_data)

