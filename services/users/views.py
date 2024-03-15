from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class UserIsNotAuthenticatedMixin(UserPassesTestMixin):
    error_is_authenticated_message = None
    error_is_authenticated_redirect_viewname = None
    request = None

    def test_func(self):
        if self.request.user.is_authenticated:
            messages.info(self.request, self.error_is_authenticated_message)
            raise PermissionDenied
        return True

    def handle_no_permission(self):
        return redirect(self.error_is_authenticated_redirect_viewname)
