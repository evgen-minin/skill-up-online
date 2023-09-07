from rest_framework.viewsets import ModelViewSet

from skilluponline.models import Course
from skilluponline.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    """
     Представление (Viewset) для работы с моделью Course.

    Параметры:
    - queryset: Запрос к базе данных для получения списка курсов.
    - serializer_class: Сериализатор, используемый для преобразования данных курсов в JSON.

    HTTP-методы:
    - GET: Получает список всех курсов.
    - POST: Создает новый курс.
    - GET (с указанным идентификатором): Получает детальную информацию о курсе.
    - PUT (с указанным идентификатором): Обновляет информацию о курсе.
    - DELETE (с указанным идентификатором): Удаляет курс.

    Поля ответа (JSON) для каждого курса:
    - id: Уникальный идентификатор курса.
    - title: Название курса.
    - preview: Ссылка на изображение-превью курса.
    - description: Описание курса.

    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
