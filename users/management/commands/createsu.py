from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            email='evgen@minin.ru',
            first_name='Admin',
            last_name='evgen',
            is_staff=True,
            is_superuser=True
        )

        if created:
            user.set_password('123qwe456rty')
            user.save()
            self.stdout.write(self.style.SUCCESS("Пользователь успешно создан."))
        else:
            self.stdout.write(self.style.SUCCESS("Пользователь уже существует."))

