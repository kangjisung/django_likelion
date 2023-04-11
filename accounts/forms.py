from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ['username', 'email']

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': '아이디 또는 비밀번호가 일치하지 않습니다.',
        'inactive': '이 계정은 비활성화 상태입니다.',
    }
