from typing import Dict, Any

import os

from django.contrib.sites import requests
from dotenv import load_dotenv

from skilluponline.models import Course, Payment
from users.models import User

# Загрузка переменных из файла .env
load_dotenv()


class StripeService:
    """
    Класс, описывающий работу с сервисом Stripe.
    Attrs:
        - api_key: Ключ для работы с API Stripe.
        - headers: Заголовки.
        - base_url: Базовый URL.
    """
    api_key = os.getenv('STRIPE_API_KEY')
    headers = {'Authorization': f'Bearer {api_key}'}
    base_url = 'https://api.stripe.com/v1'

    @classmethod
    def create_payment_intent(cls, course_id: int, user: User) -> Dict[str, Any]:
        """
        Создает платежное намерение и возвращает его данные.

        :param course_id: ID курса, который необходимо оплатить.
        :param user: Пользователь, совершающий платеж.
        """
        course = Course.get_by_id(course_id)
        amount = int(course.cost)

        data = [
            ('amount', amount * 100),
            ('currency', 'rub'),
            ('metadata[course_id]', course.id),
            ('metadata[user_id]', user.id)
        ]

        response = requests.post(f'{cls.base_url}/payment_intents', headers=cls.headers, data=data)

        if response.status_code != 200:
            raise Exception(f'Ошибка создания намерения платежа: {response.json()["error"]["message"]}')

        payment_intent = response.json()

        Payment.objects.create(
            user=user,
            paid_course=course,
            amount=course.cost,
            payment_intent_id=payment_intent['id'],
            status=payment_intent['status']
        )

        return payment_intent
