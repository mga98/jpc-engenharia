from django import forms
from django.forms import ClearableFileInput

from .models import Project, Pictures, Messages


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Digite o nome do projeto'
            }
        )
        self.fields['thumbnail'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'file',
                'onchange': 'preview()'
            }
        )

    class Meta:
        model = Project

        fields = ('title', 'thumbnail')


class PicturesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'file',
            }
        )

    class Meta:
        model = Pictures

        fields = ('image',)
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }


class MessagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }
        )

        self.fields['subject'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Assunto',
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'E-mail para contato',
            }
        )

        self.fields['message'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Sua mensagem',
            }
        )

    class Meta:
        model = Messages

        fields = ('name', 'subject', 'email', 'message')
