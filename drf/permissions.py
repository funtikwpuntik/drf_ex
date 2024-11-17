"""Module permissions"""
from rest_framework import permissions


class WarehousePermission(permissions.BasePermission):
    """Permission for Warehouse"""
    message = 'Only Warehouse user'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        type_ = request.user.type
        if type_ == 'Поставщик':
            return True

        return False


class ClientPermission(permissions.BasePermission):
    """Permission for Client"""

    message = 'Only Client user'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        type_ = request.user.type

        if type_ == 'Покупатель':
            return True

        return False
