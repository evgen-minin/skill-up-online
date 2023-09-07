from skilluponline.models import Course, Lesson
from rest_framework import serializers

from skilluponline.serializers.lesson import LessonSerializer


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
    lessons = serializers.SerializerMethodField()
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def get_lessons(self, obj):
        lessons = Lesson.objects.filter(course=obj)
        lesson_serializer = LessonSerializer(lessons, many=True)
        return lesson_serializer.data

    class Meta:
        model = Course
        fields = '__all__'
