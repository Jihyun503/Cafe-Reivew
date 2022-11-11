from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    pwd = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput()
        )
    class Meta:
        model = User
        fields = '__all__'

