from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response

from skilluponline.models import Course, CourseSubscription
from skilluponline.serializers.subscriptions import CourseSubscriptionSerializer


class CourseSubscriptionListView(ListCreateAPIView):
    """
    Представление для управления подпиской пользователя на курс.

    Параметры:
    - serializer_class: Сериализатор, используемый для преобразования данных подписки в JSON.

    HTTP-методы:
    - GET: Получает список подписок текущего пользователя на курсы.
    - POST: Создает новую подписку пользователя на курс.

    """
    serializer_class = CourseSubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        return CourseSubscription.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        serializer.save(user=user, course=course)


class CourseSubscriptionDestroyView(DestroyAPIView):
    """
     Представление для отмены подписки пользователя на курс.

    Параметры:
    - queryset: Запрос к базе данных для получения списка подписок пользователя на курсы.

    HTTP-методы:
    - DELETE: Удаляет подписку пользователя на курс.

    """
    def get_object(self):
        user = self.request.user
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        return get_object_or_404(CourseSubscription, user=user, course=course)
