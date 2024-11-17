from rest_framework import permissions


class WarehousePermission(permissions.BasePermission):
    message = 'Only Warehouse user'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        type = request.user.type
        if type == 'Поставщик':
            return True
        else:
            return False


class ClientPermission(permissions.BasePermission):
    message = 'Only Client user'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        type = request.user.type

        if type == 'Покупатель':
            return True
        else:
            return False
