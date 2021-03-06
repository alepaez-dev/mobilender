from django.db import models
from rest_framework import serializers

# Create your models here.
# In this file, we created models based on classes. We interpret every Model Class as a table in our Postgresql Database.
# This models are in order so we don't make mistakes with the foreign keys.
# Every change in this file(comments not included) will require to create a new migration and migrate it.

class Client(models.Model):
  """Client"""

  CLIENT_TYPES = (
      ("normal", "Normal"),
      ("plate", "Plate"),
      ("gold", "Gold"),
      ("platinum", "Platinum"),
  )
  name = models.CharField(max_length=150)
  type_client = models.CharField(max_length=10, choices=CLIENT_TYPES, default="normal")
  key = models.CharField(max_length=50, null=True, blank=True)
  photography = models.ImageField(null=True, blank=True)
  address = models.CharField(max_length=150)
  

  def __str__(self):
    return f"{self.name} {self.key}"

class Item(models.Model):
  """Item"""
  description = models.CharField(max_length=150)
  price = models.FloatField()

  def __str__(self):
    return f"{self.description} {self.price}"

class Provider(models.Model):
  """Provider"""
  name = models.CharField(max_length=150)
  address = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.name} {self.address}"

class ItemProvider(models.Model):
  """ItemProvider"""

  # Foreign Relations
  provider = models.ManyToManyField(Provider, blank=True, null=True, related_name="items_providers")
  item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, related_name="items_providers")

  def __str__(self):
    return f"{self.id} {self.provider} {self.item}"

class DistributionCenter(models.Model):
  warehouse = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.id} {self.warehouse}"

class AssociatedCompany(models.Model):
  references = models.CharField(max_length=150)
  client_key = models.CharField(max_length=150, null=True, blank=True)

  def __str__(self):
    return f"{self.id} {self.references}"

class Sucursal(models.Model):
  references = models.CharField(max_length=150)
  
  def __str__(self):
    return f"{self.id} {self.references}"


class Order(models.Model):
  date_created = models.DateField(auto_now_add=True)
  date_stocked = models.DateField(null=True, blank=True)
  is_urgent = models.BooleanField(default=False)

  # Foreign Relations
  client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="orders")
  distribution_center = models.ForeignKey(DistributionCenter, on_delete=models.PROTECT, related_name="orders", null=True, blank=True)
  associated_company = models.ForeignKey(AssociatedCompany, on_delete=models.PROTECT, related_name="orders",  null=True, blank=True)
  sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, related_name="orders",  null=True, blank=True)

  def __str__(self):
    return f"{self.date_created} {self.is_urgent} {self.client}"

class OrderDetail(models.Model):
  quantity = models.PositiveIntegerField()

  # Foreign Relations
  item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="orders_details")
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders_details")