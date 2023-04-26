from django import forms

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
