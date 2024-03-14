from django.contrib.sites.models import Site
from services.users.confirmation.messages import EmailValidationMessage
from services.users.confirmation.protectors.validators import UserValidator
from services.users.confirmation.views.confirmation_mixins import ConfirmValidationViewMixin
from services.users.confirmation.views.message_mixins import ValidationMessageViewMixin


class RegistrationMessage(EmailValidationMessage):
    """
    Класс, описывающий отправку сообщение валидации для регистрации
    """
    subject_template_name = "users/email/registration/subject.html"
    body_template_name = "users/email/registration/body.html"

    protocol = "http"
    domain = Site.objects.get_current().domain
    viewname = "users:registration_activation_link"


class RegistrationMessageViewMixin(ValidationMessageViewMixin):
    message_class = RegistrationMessage
    """
    Специальный класс для создания и отправки сообщения валидации
    при регистрации
    """

    def set_user_object(self, form):
        """
        Метод получения объекта при регистрации из
        формы регистрации
        """
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()


class RegistrationValidationViewMixin(ConfirmValidationViewMixin):
    """
    Класс проверки данных валидации
    при регистрации
    """
    validator_class = UserValidator
    failure_redirect_viewname = "users:registration_confirmation_failed"