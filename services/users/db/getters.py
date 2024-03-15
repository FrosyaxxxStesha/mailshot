from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode

from services.general.db.getters import SingleKwargSafeGetter

User = get_user_model()


class UserSafeGetter(SingleKwargSafeGetter):
    """
    Специализированный для пользователя класс SingleKwargSafeGetter.

    В классе определены методы для поиска по uidb64 и email.
    В случае необходимости можно унаследоваться от данного класса и добавить
    дополнительные методы для поиска объектов пользователя по ключам.
    В случае других моделей и изменения базовых методов
    лучше наследоваться от SingleKwargSafeGetter
    """
    model = User
    handler_starts_with: str = "get_user_by_"
    extra_exceptions = (model.DoesNotExists, ValidationError)

    def get_user_by_uidb64(self, uidb64: str) -> User:
        """
        Получение пользователя по uidb64
        """
        uid: bytes = urlsafe_base64_decode(uidb64)
        user: User = self.model.objects.get(pk=uid)
        return user

    def get_user_by_email(self, email: str) -> User:
        """
        Получение пользователя по email
        """
        user = self.model.objects.get(email=email)
        return user


user_safe_getter = UserSafeGetter()
