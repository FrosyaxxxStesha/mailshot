from typing import Any, Callable

from django.db.models import Model


class SingleKwargSafeGetter:
    """
    Позволяет описывать и специализировать методы для безопасного получения объекта модели по
    одному ключевому аргументу с помощью единого метода get_obj_or_none, в случае возникновения ошибки метод
    возвращает None. Дополнительные для обработки ошибки можно указывать в extra_exceptions.
    Для прописывания специфических алгоритмов получения описываются методы, имя которых соответствует шаблону:
    handler_starts_with + <имя ключевого аргумента>, например, для базового класса и поиска по pk нужно описать
    метод с именем get_by_pk
    """
    handler_starts_with: str = "get_by_"
    model: Model = None
    extra_exceptions: tuple = ()

    def get_handler(self, k: str) -> Callable:
        """
        Метод для получения обработчика поиска по имени ключевого аргумента
        """

        handler_name: str = self.handler_starts_with + k

        try:
            handler: Callable = getattr(self, handler_name)
        except AttributeError:
            raise AttributeError(f"Нет обработчика для поиска по {k}")

        return handler

    @staticmethod
    def check_kwargs(kwargs: dict) -> dict:
        """
        Проверяет единственность ключа
        """
        if len(kwargs) != 1:
            raise ValueError("метод принимает ровно один kw параметр")
        return kwargs

    def get_obj_or_none(self, **kv_pair: Any) -> Model | None:
        """
        Основной метод
        """
        kv_pair: dict = self.check_kwargs(kv_pair)
        k, *_ = kv_pair

        try:
            obj: Model | None = self.get_handler(k)(**kv_pair)
        except (TypeError, ValueError, OverflowError, *self.extra_exceptions):
            obj = None

        return obj

