from skilluponline.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course.

    Поля:
    - model: Модель, к которой применяется сериализатор - Course.
    - fields: Список полей модели, которые должны быть сериализованы (все поля модели в данном случае).

    Сериализованные поля (JSON):
    - id: Уникальный идентификатор курса.
    - title: Название курса.
    - preview: Ссылка на изображение-превью курса.
    - description: Описание курса.
    - lesson_count: Количество уроков в курсе.
    """
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return instance.lesson_set_count()

    class Meta:
        model = Course
        fields = '__all__'
