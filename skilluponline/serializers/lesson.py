from rest_framework import serializers
from skilluponline.models import Lesson
from skilluponline.validators import YoutubeLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    """
     Сериализатор для модели Lesson.

    Поля:
    - model: Модель, к которой применяется сериализатор - Lesson.
    - fields: Список полей модели, которые должны быть сериализованы (все поля модели в данном случае).

    Сериализованные поля (JSON):
    - id: Уникальный идентификатор урока.
    - title: Название урока.
    - description: Описание урока.
    - preview: Ссылка на изображение-превью урока.
    - video_link: Ссылка на видео-урок.
    - course: ID курса, к которому относится урок.
    """

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeLinkValidator(field_name='video_link')]
        extra_kwargs = {
            'preview': {'required': False}
        }