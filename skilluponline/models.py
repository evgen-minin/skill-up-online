from django.db import models


class Course(models.Model):
    """
    Модель Course представляет собой курс в образовательном приложении.

    Поля:
    - title: Название курса (максимум 150 символов).
    - preview: Изображение-превью курса (загружается в папку 'course_previews/').
    - description: Описание курса.

    Метаданные:
    - verbose_name: Название модели в единственном числе - 'Курс'.
    - verbose_name_plural: Название модели во множественном числе - 'Курсы'.
    """
    title = models.CharField(max_length=150)
    preview = models.ImageField(upload_to='course_previews/')
    description = models.TextField

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
     Модель Lesson представляет собой урок в рамках курса.

    Поля:
    - title: Название урока (максимум 150 символов).
    - description: Описание урока.
    - preview: Изображение-превью урока (загружается в папку 'lesson_preview/').
    - video_link: Ссылка на видео-урок.

    Внешний ключ:
    - course: Связь с курсом, к которому относится урок (связь "один-ко-многим").

    Метаданные:
    - verbose_name: Название модели в единственном числе - 'Урок'.
    - verbose_name_plural: Название модели во множественном числе - 'Уроки'.
    """
    title = models.CharField(max_length=150)
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson_preview/')
    video_link = models.URLField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
