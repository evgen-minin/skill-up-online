from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class LoginForm(forms.Form):
    """
    Форма для входа пользователя.

    Поля:
    - email: Поле для ввода электронной почты пользователя.
    - password: Поле для ввода пароля пользователя (скрыто при вводе).
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    """
     Форма для регистрации нового пользователя.

    Поля:
    - email: Поле для ввода электронной почты пользователя.
    - password1: Поле для ввода пароля пользователя (первый раз).
    - password2: Поле для ввода пароля пользователя (повторно для подтверждения).
    """
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """
     Форма для редактирования профиля пользователя.

    Поля:
    - email: Поле для ввода электронной почты пользователя.
    - first_name: Поле для ввода имени пользователя.
    - last_name: Поле для ввода фамилии пользователя.
    - phone_number: Поле для ввода номера телефона пользователя.
    - avatar: Поле для загрузки изображения-аватара пользователя.
    - country: Поле для выбора страны пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget = forms.HiddenInput()
        