from rest_framework.routers import DefaultRouter

from drf.models import Warehouse
from drf.views import UserModelViewSet, WarehouseModelViewSet, ProductModelViewSet, OrderModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('products', ProductModelViewSet)
router.register('warehouses', WarehouseModelViewSet)
router.register('orders', OrderModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)