from django.db import models
# from rest_framework import serializers

# Create your models here.

class Client(models.Model):
  """Client"""
  name = models.CharField(max_length=150)
  key = models.CharField(max_length=50)
  photography = models.CharField(max_length=255, null=True, blank=True)
  address = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.name} {self.key}"

class Provider(models.Model):
  """Provider"""
  name = models.CharField(max_length=150)
  address = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.name} {self.address}"