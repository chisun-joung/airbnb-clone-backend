from strawberry.permission import BasePermission
from strawberry.types import Info
import typing


class OnlyLoggedIn(BasePermission):
    message = "You must be logged in to see this."

    def has_permission(self, source: typing.Any, info: Info):
        return info.context.request.user.is_authenticated
