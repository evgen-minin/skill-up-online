from rest_framework import serializers

from skilluponline.models import CourseSubscription


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CourseSubscription.

    Поля:
    - model: Модель, к которой применяется сериализатор - CourseSubscription.
    - fields: Список полей модели, которые должны быть сериализованы (поле 'subscribed' в данном случае).

    Сериализованные поля (JSON):
    - subscribed: Флаг, указывающий, подписан пользователь на обновления курса или нет.

    """
    class Meta:
        model = CourseSubscription
        fields = ['subscribed']
