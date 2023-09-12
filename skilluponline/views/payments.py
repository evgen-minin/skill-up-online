import django_filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from skilluponline.models import Payment
from skilluponline.serializers.payments import PaymentSerializer, PaymentIntentCreateSerializer

from rest_framework import generics

from skilluponline.stripe_api_service import StripeService
from rest_framework.response import Response
from rest_framework.views import Request


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


class PaymentIntentCreateView(generics.CreateAPIView):
    serializer_class = PaymentIntentCreateSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            201: openapi.Response('Payment successful', PaymentSerializer),
            400: 'Payment failed'
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Создает платежное намерение"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            course_id = serializer.validated_data['course_id']
            user = request.user
            try:
                payment_intent = StripeService.create_payment_intent(course_id, user)
                payment = Payment.get_by_payment_intent_id(payment_intent_id=payment_intent['id'])
                payment_serializer = PaymentSerializer(payment)
                return Response(payment_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
