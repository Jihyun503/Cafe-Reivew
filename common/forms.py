from django import forms
from .models import User
from asyncio import exceptions

from argon2 import PasswordHasher

class SignupForm(forms.ModelForm):
    pwd = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput()
        )
    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.Form):
    email = forms.EmailField()
    pwd = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput()
        )

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        pwd = cleaned_data.get('pwd')
        
        if email and pwd:
            try:
                user = User.objects.get(email = email)
                print(user.email)
                print(user.pwd)
            except User.DoesNotExist:
                return self.add_error("email", "아이디가 존재하지 않습니다.")
            
            if pwd != user.pwd: 
                return self.add_error("pwd", "비밀번호가 틀렸습니다.")
            else:
                self.email = email
    