from django import forms
from django.forms import ClearableFileInput

from .models import Project, Pictures


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
    class Meta:
        model = Pictures

        fields = ('image',)
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }
