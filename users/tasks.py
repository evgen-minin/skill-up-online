from datetime import datetime, timedelta

from celery import shared_task

from skilluponline.models import Payment
from users.models import User


@shared_task
def check_payment_status():
    payment_list = Payment.objects.filter(status__in=[Payment.status_new, Payment.status_handle])
    for payment_item in payment_list:
        print('check payment status')


@shared_task
def check_inactive_users():
    # Определяем дату, которая считается "более месяца назад"
    one_month_ago = datetime.now() - timedelta(days=30)

    # Получаем список пользователей, которые не заходили в систему более месяца
    inactive_users = User.objects.filter(last_login__lte=one_month_ago)

    # Блокируем пользователей, устанавливая флаг is_active в False
    for user in inactive_users:
        user.is_active = False
        user.save()
