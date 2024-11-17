"""Module Views"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf.models import ApiUser, Warehouse, Product, Order
from drf.permissions import WarehousePermission, ClientPermission
from drf.serializers import UserSerializer, WarehouseSerializer, ProductSerializer, OrderSerializer


# Create your views here.

# pylint: disable=all
class UserModelViewSet(viewsets.ModelViewSet):
    """User model view"""
    queryset = ApiUser.objects.all()
# pylint: enable=all
    http_method_names = ['post', 'patch', 'get']
    serializer_class = UserSerializer
# pylint: disable=all

class WarehouseModelViewSet(viewsets.ModelViewSet):
    """Warehouse model view"""
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
# pylint: enable=all
    permission_classes = [IsAuthenticated, WarehousePermission]

# pylint: disable=all
class ProductModelViewSet(viewsets.ModelViewSet):
    """Product model view"""
    queryset = Product.objects.all()
# pylint: enable=all
    serializer_class = ProductSerializer
    http_method_names = ['post', 'patch', 'get', 'put']
    permission_classes = [IsAuthenticated, WarehousePermission]

# pylint: disable=all
class OrderModelViewSet(viewsets.ModelViewSet):
    """Order model view"""
    queryset = Order.objects.all()
# pylint: enable=all
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
