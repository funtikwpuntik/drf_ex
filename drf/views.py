from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf.models import ApiUser, Warehouse, Product, Order
from drf.permissions import WarehousePermission, ClientPermission
from drf.serializers import UserSerializer, WarehouseSerializer, ProductSerializer, OrderSerializer


# Create your views here.


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()

    http_method_names = ['post', 'patch', 'get']
    serializer_class = UserSerializer


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    permission_classes = [IsAuthenticated, WarehousePermission]

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', 'patch', 'get', 'put']
    permission_classes = [IsAuthenticated, WarehousePermission]

class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ClientPermission]


