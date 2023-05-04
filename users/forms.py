# flake8: noqa

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.forms_utils import add_attr


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields['username'], 'placeholder', 'Nome de usuário')
        add_attr(self.fields['username'], 'class', 'form-control')
        add_attr(self.fields['username'], 'autofocus', 'autofocus')

        add_attr(self.fields['password'], 'placeholder', 'Digite sua senha')
        add_attr(self.fields['password'], 'class', 'form-control')

    username = forms.CharField(label='Usuário')
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
    )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        first_name_field = self.fields['first_name']
        last_name_field = self.fields['last_name']
        username_field = self.fields['username']
        password_field = self.fields['password']
        password_2_field = self.fields['password_2']
        email_field = self.fields['email']

        add_attr(first_name_field, 'class', 'form-control')
        add_attr(first_name_field, 'placeholder', 'Primeiro nome')

        add_attr(last_name_field, 'class', 'form-control')
        add_attr(last_name_field, 'placeholder', 'Último nome')

        add_attr(email_field, 'class', 'form-control')
        add_attr(email_field, 'placeholder', 'E-mail')

        add_attr(username_field, 'class', 'form-control')
        add_attr(username_field, 'placeholder', 'Nome de usuário')

        add_attr(password_field, 'class', 'form-control')
        add_attr(password_field, 'placeholder', 'Senha')

        add_attr(password_2_field, 'class', 'form-control')
        add_attr(password_2_field, 'placeholder', 'Confirme a senha')

    first_name = forms.CharField(
        error_messages={'required': 'Você precisa preencher o campo de primeiro nome!'},
        label='Primeiro nome'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Você precisa preencher o campo de último nome!'},
        label='Último nome'
    )

    email = forms.CharField(
        error_messages={'required': 'Você precisa preencher o campo de E-mail!'},
        label='E-mail',
    )

    username = forms.CharField(
        label='Nome de usuário',
        error_messages={'required': 'É necessário um nome de usuário!'}
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Você precisa preencher o campo de senha!'}
    )

    password_2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Você precisa confirmar a senha!'}
    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_2')

        if password != password_2:
            password_confirmation_error = ValidationError(
                'Verifique se as senhas são iguais',
                code='invalid'
            )

            raise ValidationError({
                'password': password_confirmation_error,
                'password_2': [
                    password_confirmation_error
                ],
            })
