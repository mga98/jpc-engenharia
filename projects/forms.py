from django import forms
from django.forms import ClearableFileInput

from .models import Project, Pictures


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = ('title', 'status', 'thumbnail')


class PicturesForm(forms.ModelForm):
    class Meta:
        model = Pictures

        fields = ('image',)
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }
