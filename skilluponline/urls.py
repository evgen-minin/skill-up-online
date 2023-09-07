from django.urls import path
from rest_framework import routers

from skilluponline.views.course import CourseViewSet
from skilluponline.views.lesson import LessonCreateView, LessonDeleteView, LessonDetailView, LessonListView, \
    LessonUpdateView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
