from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from skilluponline.models import Course


class LessonTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            email='evgen@minin.ru',
            first_name='Admin',
            last_name='evgen',
            is_staff=True,
            is_superuser=True,
        )
        self.user.set_password('123qwe456rty')
        self.user.save()

        self.course = Course.objects.create(
            user=self.user,
            title='Existing Course',
            description='Existing Description'
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test1Lesson',
            'description': 'Test1Lesson',
            'video_link': 'https://www.youtube.com/watch?v=abc123',
            'course': self.course.id,
            'user': self.user.id
        }
        response = self.client.post(
            '/lessons/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
