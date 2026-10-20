from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(max_length=30, required=False, label="Nombre")
    last_name = forms.CharField(max_length=30, required=False, label="Apellido")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        labels = {'imagen': 'Seleccionar foto de perfil'}