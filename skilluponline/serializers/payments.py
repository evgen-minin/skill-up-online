from rest_framework import serializers

from skilluponline.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Payment.

    Поля:
    - model: Модель, к которой применяется сериализатор - Payment.
    - fields: Список полей модели, которые должны быть сериализованы (все поля модели в данном случае).

    Сериализованные поля (JSON):
    - id: Уникальный идентификатор платежа.
    - user: Пользователь, совершивший платеж.
    - date: Дата и время платежа.
    - course_or_lesson: Курс или урок, за который был сделан платеж.
    - amount: Сумма оплаты в формате DecimalField.
    - payment_method: Способ оплаты, выбирается из списка (наличные, перевод на счет).
    """
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentIntentCreateSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()
