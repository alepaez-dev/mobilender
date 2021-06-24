"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    #Client 
    path('api/client/', ListClientAPIView.as_view(), name = "list_clients"),
    path('api/client/create/', CreateClientAPIView.as_view(), name = "create_clients"),
    #Provider
    path('api/provider/', ListProviderAPIView.as_view(), name = "list_providers"),
    path('api/provider/create/', CreateProviderAPIView.as_view(), name = "create_provider"),
    #Item
    path('api/item/', ListItemAPIView.as_view(), name = "list_items"),
    path('api/item/create/', CreateItemAPIView.as_view(), name = "create_item"),
    #ItemProvider
    path('api/itemprovider/', ListItemProviderAPIView.as_view(), name = "list_items_providers"),
    #DistributionCenter
    path('api/distribution_center/', ListDistributionCenterAPIView.as_view(), name = "list_distribution_centers"),
    path('api/distribution_center/create/', CreateDistributionCenterAPIView.as_view(), name = "create_distribution_center"),
    #AssociatedCompany
    path('api/associated_company/', ListAssociatedCompanyAPIView.as_view(), name = "list_associated_company"),
    path('api/associated_company/create/', CreateAssociatedCompanyAPIView.as_view(), name = "create_associated_companies"),
    #Sucursal
    path('api/sucursal/', ListSucursalAPIView.as_view(), name = "list_sucursal"),
    path('api/sucursal/create/', CreateSucursalAPIView.as_view(), name = "create_sucursal"),
    #Order
    path('api/order/', ListOrderAPIView.as_view(), name = "list_orders"),
    path('api/order/platinum/', ListSpecialPlatinumOrdersAPIView.as_view(), name = "list_special_orders"),
    path('api/order/create/', CreateOrderAPIView.as_view(), name = "create_order"),
    path('api/order/<int:pk>/', RetrieveOrderAPIView.as_view(), name = "retrieve_order"),
    path('api/order/<int:pk>/update/', UpdateOrderAPIView.as_view(), name = "update_order"),
    #OrderDetail
    path('api/orderdetail/', ListOrderDetailAPIView.as_view(), name = "list_order_details"),
    path('api/orderdetail/create/', CreateOrderDetailAPIView.as_view(), name = "create_order_details"),
]
