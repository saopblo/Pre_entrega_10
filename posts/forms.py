
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado', 'imagen']
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'estado': 'Estado',
            'imagen': 'Imagen',
        }
        