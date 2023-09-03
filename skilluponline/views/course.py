from rest_framework.viewsets import ModelViewSet 

from skilluponline.models import Course
from skilluponline.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer