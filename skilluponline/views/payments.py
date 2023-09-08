from rest_framework import generics, filters
import django_filters

from skilluponline.models import Payment


class PaymentFilter(django_filters.FilterSet):
    payment_date = django_filters.DateFromToRangeFilter()
    paid_course_or_lesson = django_filters.CharFilter(lookup_expr='содержит')
    payment_method = django_filters.CharFilter(lookup_expr='способ_оплаты')

    class Meta:
        model = Payment
        fields = ['payment_date', 'paid_course_or_lesson', 'payment_method']


class PaymentSerializer:
    pass


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.DjangoFilterBackend]
    ordering_fields = ['payment_date']
    filterset_class = PaymentFilter
