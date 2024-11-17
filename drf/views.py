"""Module Views"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf.models import ApiUser, Warehouse, Product, Order
from drf.permissions import WarehousePermission, ClientPermission
from drf.serializers import UserSerializer, WarehouseSerializer, ProductSerializer, OrderSerializer


# Create your views here.


class UserModelViewSet(viewsets.ModelViewSet):
    """User model view"""
    queryset = ApiUser.objects.all()

    http_method_names = ['post', 'patch', 'get']
    serializer_class = UserSerializer


class WarehouseModelViewSet(viewsets.ModelViewSet):
    """Warehouse model view"""
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    permission_classes = [IsAuthenticated, WarehousePermission]


class ProductModelViewSet(viewsets.ModelViewSet):
    """Product model view"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', 'patch', 'get', 'put']
    permission_classes = [IsAuthenticated, WarehousePermission]


class OrderModelViewSet(viewsets.ModelViewSet):
    """Order model view"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
