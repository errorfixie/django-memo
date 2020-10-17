from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):

        username = forms.CharField(
            label= "ID",
            widget=forms.TextInput(
                attrs={
                    # "class":"여기에 css적용"
                }
            )
        )

        password1 = forms.CharField(
            label="비밀번호",
            widget=forms.PasswordInput(
                attrs={
                    # "class":"여기에 css적용"
                }
            )
        )

        password2 = forms.CharField(
            label="비밀번호확인",
            widget=forms.PasswordInput(
                attrs={
                    # "class":"여기에 css적용"
                }
            )
        )
        class Meta:
            model = User
            fields = ('username',
                        'email',
                        'nickname', 
                        'password1', 
                        'password2',
                    )
            
            labels ={
                "nickname":"별명",
                "email":"이메일",
            }
            
            widgets = {
                "nickname" : forms.TextInput(
                        attrs={
                            # "class":"여기에 css적용"
                        }
                    ),
                "email" : forms.EmailInput(
                        attrs={
                            # "class":"여기에 css적용"
                        }
                    )
            }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        label="ID",
        widget=forms.TextInput(
            attrs={
                # "class":"여기에 css적용"
            }
        )
    )
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                # "class":"여기에 css적용"
            }
        )
    )