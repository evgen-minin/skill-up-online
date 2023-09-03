from django.urls import path

from users.apps import UsersConfig
from users.views import ConfirmView, LoginView, LogoutView, RegisterView, ProfileView, generate_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/gen_password', generate_password, name='generate_password'),
    path('success_register/<register_uuid>', ConfirmView.as_view(), name='success_register'),
]
