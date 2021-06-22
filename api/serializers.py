
from rest_framework import serializers
import os

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
