from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from skilluponline.models import Lesson
from skilluponline.permissions import IsModerator
from skilluponline.serializers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
    """
    Представление для получения детальной информации об уроке.

    Параметры:
    - queryset: Запрос к базе данных для получения списка уроков.
    - serializer_class: Сериализатор, используемый для преобразования данных урока в JSON.

    HTTP-методы:
    - GET: Получает детальную информацию об уроке с определенным ID.

    Поля ответа (JSON):
    - id: Уникальный идентификатор урока.
    - title: Название урока.
    - description: Описание урока.
    - preview: Ссылка на изображение-превью урока.
    - video_link: Ссылка на видео-урок.
    - course: ID курса, к которому относится урок.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListView(ListAPIView):
    """
    Представление для получения списка всех уроков.

    Параметры:
    - queryset: Запрос к базе данных для получения списка уроков.
    - serializer_class: Сериализатор, используемый для преобразования данных уроков в JSON.

    HTTP-методы:
    - GET: Получает список всех уроков.

    Поля ответа (JSON) для каждого урока:
    - id: Уникальный идентификатор урока.
    - title: Название урока.
    - description: Описание урока.
    - preview: Ссылка на изображение-превью урока.
    - video_link: Ссылка на видео-урок.
    - course: ID курса, к которому относится урок.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]


class LessonUpdateView(RetrieveUpdateAPIView):
    """
    Представление для обновления информации об уроке.

    Параметры:
    - queryset: Запрос к базе данных для получения списка уроков.
    - serializer_class: Сериализатор, используемый для преобразования данных урока в JSON.

    HTTP-методы:
    - GET: Получает детальную информацию об уроке с определенным ID.
    - PUT: Обновляет информацию об уроке с определенным ID.

    Поля запроса (JSON):
    - title: Название урока.
    - description: Описание урока.
    - preview: Ссылка на изображение-превью урока.
    - video_link: Ссылка на видео-урок.

    Поля ответа (JSON):
    - id: Уникальный идентификатор урока.
    - title: Название урока (обновленное значение).
    - description: Описание урока (обновленное значение).
    - preview: Ссылка на изображение-превью урока (обновленное значение).
    - video_link: Ссылка на видео-урок (обновленное значение).
    - course: ID курса, к которому относится урок.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]


class LessonCreateView(CreateAPIView):
    """
    Представление для создания нового урока.

    Параметры:
    - queryset: Запрос к базе данных для получения списка уроков.
    - serializer_class: Сериализатор, используемый для преобразования данных урока в JSON.

    HTTP-методы:
    - POST: Создает новый урок.

    Поля запроса (JSON):
    - title: Название урока.
    - description: Описание урока.
    - preview: Ссылка на изображение-превью урока.
    - video_link: Ссылка на видео-урок.

    Поля ответа (JSON):
    - id: Уникальный идентификатор созданного урока.
    - title: Название урока.
    - description: Описание урока.
    - preview: Ссылка на изображение-превью урока.
    - video_link: Ссылка на видео-урок.
    - course: ID курса, к которому относится урок.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]


class LessonDeleteView(DestroyAPIView):
    """
     Представление для удаления урока.

    Параметры:
    - queryset: Запрос к базе данных для получения списка уроков.
    - serializer_class: Сериализатор, используемый для преобразования данных урока в JSON.

    HTTP-методы:
    - DELETE: Удаляет урок с определенным ID.

    Поля ответа (JSON):
    - Успешное удаление возвращает пустой ответ (status 204).
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]
