from django import forms
from django.forms import ClearableFileInput

from .models import Project, Pictures, Messages
from utils.forms_utils import add_attr


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        title_field = self.fields['title']
        thumbnail_field = self.fields['thumbnail']

        add_attr(title_field, 'class', 'form-control')
        add_attr(title_field, 'placeholder', 'Digite o nome do projeto')

        add_attr(thumbnail_field, 'class', 'form-control')
        add_attr(thumbnail_field, 'type', 'file')
        add_attr(thumbnail_field, 'onchange', 'preview()')

    class Meta:
        model = Project

        fields = ('title', 'thumbnail')


class PicturesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        image_field = self.fields['image']

        add_attr(image_field, 'class', 'form-control')
        add_attr(image_field, 'type', 'file')

    class Meta:
        model = Pictures

        fields = ('image',)
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }


class MessagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name_field = self.fields['name']
        subject_field = self.fields['subject']
        email_field = self.fields['email']
        message_field = self.fields['message']

        add_attr(name_field, 'class', 'form-control')
        add_attr(name_field, 'placeholder', 'Nome completo')

        add_attr(subject_field, 'class', 'form-control')
        add_attr(subject_field, 'placeholder', 'Assunto')

        add_attr(email_field, 'class', 'form-control')
        add_attr(email_field, 'placeholder', 'E-mail para contato')

        add_attr(message_field, 'class', 'form-control')
        add_attr(message_field, 'placeholder', 'Sua mensagem')

    class Meta:
        model = Messages

        fields = ('name', 'subject', 'email', 'message')
