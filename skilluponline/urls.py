from django.urls import path
from rest_framework import routers

from skilluponline.views.course import CourseViewSet
from skilluponline.views.lesson import LessonCreateView, LessonDeleteView, LessonDetailView, LessonListView, \
    LessonUpdateView
from skilluponline.views.payments import PaymentListAPIView, PaymentIntentCreateView
from skilluponline.views.subscriptions import CourseSubscriptionListView, CourseSubscriptionDestroyView

app_name = 'skilluponline'

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('courses/<int:course_id>/subscribe/', CourseSubscriptionListView.as_view(), name='course-subscribe'),
    path('courses/<int:course_id>/unsubscribe/', CourseSubscriptionDestroyView.as_view(), name='course-unsubscribe'),
    path('create_payment_intent/', PaymentIntentCreateView.as_view(), name='create-payment-intent'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
