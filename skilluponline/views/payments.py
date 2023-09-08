import django_filters
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from skilluponline.models import Payment


class PaymentFilter(django_filters.FilterSet):
    payment_date_after = django_filters.DateFilter(field_name='date')
    payment_date_before = django_filters.DateFilter(field_name='date')
    paid_course_or_lesson = django_filters.CharFilter(field_name='course_or_lesson__title', lookup_expr='содержит')
    payment_method = django_filters.CharFilter(field_name='payment_method', lookup_expr='Способ оплаты')

    class Meta:
        model = Payment
        fields = []


class PaymentSerializer:
    pass


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date']
    filterset_class = PaymentFilter
