import django_filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from skilluponline.models import Payment
from skilluponline.serializers.payments import PaymentSerializer


class PaymentFilter(django_filters.FilterSet):
    payment_date_after = django_filters.DateFilter(field_name='date')
    payment_date_before = django_filters.DateFilter(field_name='date')
    paid_course_or_lesson = django_filters.CharFilter(field_name='course_or_lesson__title', lookup_expr='содержит')
    payment_method = django_filters.CharFilter(field_name='payment_method', lookup_expr='Способ оплаты')

    class Meta:
        model = Payment
        fields = []


class PaymentListAPIView(ListAPIView):
    """
    Представление для получения списка платежей с возможностью фильтрации и сортировки.

    Параметры:
    - queryset: Запрос к базе данных для получения списка платежей.
    - serializer_class: Сериализатор, используемый для преобразования данных платежей в JSON.
    - filter_backends: Список фильтров и способов сортировки, используемых для запросов.
    - ordering_fields: Поля, по которым можно сортировать список платежей.
    - filterset_class: Класс фильтра для применения фильтрации к данным.

    Фильтры:
    - payment_date_after: Фильтрация по дате платежа (платежи после указанной даты).
    - payment_date_before: Фильтрация по дате платежа (платежи до указанной даты).
    - paid_course_or_lesson: Фильтрация по названию курса или урока (платежи, содержащие указанный текст).
    - payment_method: Фильтрация по способу оплаты (без учета регистра).

    HTTP-методы:
    - GET: Получает список всех платежей с возможностью фильтрации и сортировки.

    Поля ответа (JSON) для каждого платежа:
    - user: Идентификатор пользователя, который сделал платеж.
    - date: Дата и время платежа.
    - course_or_lesson: Название курса или урока, за который был сделан платеж.
    - amount: Сумма оплаты.
    - payment_method: Способ оплаты.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date']
    filterset_class = PaymentFilter
