from django.core.management.base import BaseCommand
from datetime import datetime

from skilluponline.models import Payment, Course
from users.models import User


class Command(BaseCommand):
    help = 'Creates sample payment data'

    def handle(self, *args, **kwargs):
        user = User.objects.get(username='evgen')
        your_course_or_lesson_instance = Course.objects.get(
            id=1)
        payment = Payment.objects.create(
            user=user,
            date=datetime.now(),
            course_or_lesson=your_course_or_lesson_instance,
            amount=100.00,
            payment_method='cash'
        )
        self.stdout.write(self.style.SUCCESS(f'Платёж успешно создан: {payment.id}'))
