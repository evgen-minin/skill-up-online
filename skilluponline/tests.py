from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework import status
from rest_framework.test import APITestCase

from skilluponline.models import Course, Lesson


class LessonCreateTest(APITestCase):

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


class LessonDeleteTest(APITestCase):
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

        self.lesson = Lesson.objects.create(
            user=self.user,
            title='Test1Lesson',
            description='Test1Lesson',
            video_link='https://www.youtube.com/watch?v=abc123',
            course=self.course,
        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            f'/lessons/{self.lesson.id}/delete/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())


class LessonUpdateTest(APITestCase):
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

        self.lesson_data = {
            'title': 'Test1Lesson',
            'description': 'Test1Lesson',
            'preview': 'https://example.com/preview.jpg',
            'video_link': 'https://www.youtube.com/watch?v=abc123',
            'course': self.course,
            'user': self.user
        }

        self.lesson = Lesson.objects.create(**self.lesson_data)

    def test_update_lesson(self):
        """ Тестирование обновления урока """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Updated Lesson',
            'description': 'This is an updated lesson',
            'video_link': 'https://www.youtube.com/watch?v=updated123',
            'course': self.course.id,
            'user': self.user.id
        }
        response = self.client.put(
            f'/lessons/{self.lesson.id}/update/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, data['title'])
        self.assertEqual(self.lesson.description, data['description'])
        self.assertEqual(self.lesson.video_link, data['video_link'])


class LessonListViewTest(APITestCase):
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

        self.lesson = Lesson.objects.create(
            user=self.user,
            title='Test1Lesson',
            description='Test1Lesson',
            video_link='https://www.youtube.com/watch?v=abc123',
            course=self.course,
        )

    def test_list_lessons(self):
        """ Тестирование на отображение урока """
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/lessons/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(len(response.data), 4)
