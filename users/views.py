import random
import uuid
from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView, CreateView, TemplateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserProfileForm, UserCreationForm

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages

from users.models import User


class LoginView(BaseLoginView):
    """
    Представление для входа пользователя.

    Параметры:
    - template_name: Имя шаблона для страницы входа.
    """
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    """
     Представление для выхода пользователя.
    """
    pass


class RegisterView(CreateView):
    """
     Представление для регистрации нового пользователя.

    Параметры:
    - model: Модель пользователя (User).
    - form_class: Форма регистрации (UserRegisterForm).
    - template_name: Имя шаблона для страницы регистрации.
    - success_url: URL-адрес, на который перенаправляется пользователь после успешной регистрации.

    Методы:
    - form_valid(self, form): Метод, выполняющийся при успешной валидации формы регистрации.
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.register_uuid = uuid.uuid4().hex
            self.object.save()
            current_site = get_current_site(self.request)
            send_mail(
                subject='Подтверждение аккаунта',
                message=f'Для подтверждения перейдите по ссылке http://{current_site}{reverse_lazy("users:success_register", kwargs={"register_uuid": self.object.register_uuid})}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
            return super().form_valid(form)


class ConfirmView(TemplateView):
    """
     Представление для подтверждения аккаунта пользователя.
    """

    def get(self, request, *args, **kwargs):
        if kwargs.get('register_uuid'):
            user = User.objects.filter(register_uuid=kwargs['register_uuid']).first()
            if user:
                user.is_active = True
                user.save()
                messages.add_message(request, messages.INFO, f'Учетная запись {user.email} активирована')
        return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    """
    Представление для редактирования профиля пользователя.

    Параметры:
    - model: Модель пользователя (User).
    - form_class: Форма редактирования профиля (UserProfileForm).
    - success_url: URL-адрес, на который перенаправляется пользователь после успешного обновления профиля.

    Методы:
    - get_object(self, queryset=None): Метод, получающий объект пользователя для редактирования (текущего пользователя).
    """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    """
     Функция для генерации нового пароля и отправки его на электронную почту пользователя.
    """
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('skillup'))
