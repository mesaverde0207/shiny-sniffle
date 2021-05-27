from __future__ import annotations
from typing import TYPE_CHECKING
from django.contrib.auth.models import User

if TYPE_CHECKING:
    from django.http import HttpRequest


class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request: HttpRequest, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
