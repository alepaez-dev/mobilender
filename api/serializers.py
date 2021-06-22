
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
      "name",
      "address"
    ]



class ItemProviderSerializer(serializers.ModelSerializer):
  """ItemProvider"""
  # provider = ProviderSerializer()
  # item = ItemSerializer()
  class Meta:
    model = ItemProvider
    fields = [
      "provider",
      "item"
    ]

class ItemSerializer(serializers.ModelSerializer):
  """Item"""
  items_providers = ItemProviderSerializer(many=True)
  class Meta:
    model = Item
    fields = [
      "description",
      "price",
      "items_providers"
    ]
class ItemProviderSerializerr(serializers.ModelSerializer):
  """ItemProvider"""
  provider = ProviderSerializer()
  item = ItemSerializer()
  class Meta:
    model = ItemProvider
    fields = [
      "provider",
      "item"
    ]

class ItemProvider_ProviderSerializerr(serializers.ModelSerializer):
  """ItemProvider"""
  provider = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
  # provider = ProviderSerializer()
  class Meta:
    model = ItemProvider
    fields = [
      "provider",
    ]
class CreateItemSerializer(serializers.ModelSerializer):
  """Item"""
  items_providers = ItemProvider_ProviderSerializerr()
  class Meta:
    model = Item
    fields = [
      "description",
      "price",
      "items_providers"
    ]
  def create(self, validated_data):
    print("aqui")
    print(validated_data)