from django import forms

from .models import Post
from .models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user_id', 'content']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput())

