from django.db import models

from users.models import User


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
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def save(self, *args, **kwargs):
        from skilluponline.tasks import send_notify_update
        if self.pk is not None:
            send_notify_update.delay(self.pk)
        super().save(*args, **kwargs)

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
    preview = models.ImageField(upload_to='lesson_preview/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    """
    Модель "Платежи" для отслеживания платежей пользователей за курсы или уроки.

    Поля:
    - user: Связь с пользователем, который сделал платеж.
    - date: Дата и время платежа.
    - course_or_lesson: Связь с курсом или уроком, за который был сделан платеж.
    - amount: Сумма оплаты в формате DecimalField.
    - payment_method: Способ оплаты, выбирается из списка (наличные, перевод на счет).
    - payment_intent_id: 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    course_or_lesson = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method_choices = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счёт'),
    ]
    payment_method = models.CharField(max_length=10, choices=payment_method_choices)
    payment_intent_id = models.CharField(max_length=255, unique=True)

    @classmethod
    def get_by_payment_intent_id(cls, payment_intent_id):
        matching_payments = cls.objects.filter(payment_intent_id=payment_intent_id)
        if matching_payments.exists():
            return matching_payments.first()
        else:
            return None


class CourseSubscription(models.Model):
    """
    Модель "Подписка на обновления курса" для отслеживания подписок пользователей на курсы.

    Поля:
    - user: Связь с пользователем, который подписан на курс.
    - course: Связь с курсом, на который пользователь подписан.
    - subscribed: Флаг, указывающий, подписан пользователь на обновления курса или нет (по умолчанию False).

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)
