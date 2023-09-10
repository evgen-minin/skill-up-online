import re

from rest_framework.exceptions import ValidationError


class YoutubeLinkValidator:
    """
    Валидатор ссылок на видео YouTube.

    Этот валидатор проверяет, что значение поля является допустимой ссылкой на видео YouTube.

    Параметры:
    - field_name (str): Имя поля, для которого выполняется валидация.

    Методы:
    - __call__: Вызывается при валидации значения поля.
    """
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        youtube_pattern = r"https://www.youtube.com/.*"
        if not re.search(youtube_pattern, value[self.field_name]):
            raise ValidationError(f"Ссылка {self.field_name} должна вести на YouTube")
