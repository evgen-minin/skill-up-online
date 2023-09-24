from celery import shared_task
from django.core.mail import send_mail

from skilluponline.models import CourseSubscription


@shared_task
def send_notify_update(course_pk):
    course_list = CourseSubscription.objects.filter(course_id=course_pk)
    for course_item in course_list:
        print('! send_email')
        send_mail(
            subject=f'Обновление курса {course_item.course_title}',
            message=f'Обновление курса {course_item.course_title}',
            recipient_list=[course_item.user.email],
            from_email='evgenminin1988@mail.ru'
        )
