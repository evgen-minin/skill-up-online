
import random
import uuid
from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView, CreateView, TemplateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserProfileForm, UserCreationForm
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.http import HttpResponse


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
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
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('register_uuid'):
            user = User.objects.filter(register_uuid=kwargs['register_uuid']).first()
            if user: 
                user.is_active = True
                user.save()
                messages.add_message(request, messages.INFO, f'Учетная запись {user.email} активирована')
        return redirect(reverse('users:login'))
    
    
    
class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    
def generate_password(request):
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
    