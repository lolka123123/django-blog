from django import forms
from .models import Article, Comment, Profile

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Написать комментарий',
                'cols': '50',
                'rows': '5',
            })
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '30',
                'rows': '10'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control'
            })

        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '30',
                'rows': '10'
            })
        }