from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView

from services import (RegistrationMessageViewMixin,
                      ActiveUrlMixin,
                      UserIsNotAuthenticatedMixin,
                      RegistrationValidationViewMixin)
# Create your views here.

from django.contrib.auth import get_user_model

from users.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm

User = get_user_model()


# Регистрация

class RegistrationView(ActiveUrlMixin, UserIsNotAuthenticatedMixin, RegistrationMessageViewMixin, CreateView):
    model = User
    form_class = RegistrationForm
    active_url = "register"
    template_name = "users/registration/form.html"

    def get_success_url(self):
        return reverse("users:registration_email_sent")


class RegistrationEmailSentTemplateView(UserIsNotAuthenticatedMixin, TemplateView):
    template_name = "users/registration/email_sent.html"


class RegistrationValidationView(UserIsNotAuthenticatedMixin, RegistrationValidationViewMixin, TemplateView):
    template_name = "users/registration/success.html"

    def success_handler(self, request, *args, **kwargs):
        self.finish_validation()
        return super().success_handler(request, *args, **kwargs)


class RegistrationFailedView(UserIsNotAuthenticatedMixin, TemplateView):
    template_name = "users/registration/failed.html"


# Вход и выход


class UserLoginView(ActiveUrlMixin, UserIsNotAuthenticatedMixin, LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    active_url = "login"


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


# Сброс пароля


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = "users/reset/form.html"
    success_url = reverse_lazy("users:reset_email_sent")
    subject_template_name = "users/reset/email/subject.txt"
    email_template_name = "users/reset/email/mail.html"


class ResetEmailSentTemplateView(TemplateView):
    template_name = "users/reset/email_sent.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = "users/reset/set_password_form.html"
    success_url = reverse_lazy("users:password_reset_complete")
    post_reset_login = True


class ResetCompleteTemplateView(TemplateView):
    template_name = "users/reset/complete.html"


