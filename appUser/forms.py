from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """RegisterForm definition."""
    # TODO: Define form fields here
    email = forms.EmailField()
    last_name=forms.CharField(label="Apellidos",max_length=80)
    first_name=forms.CharField(label="Nombres",max_length=80)
    class Meta:
        model=User #USER DE DJANGO
        fields=['last_name','first_name','username','email','password1','password2']

class LoginForm(forms.Form):
    """LoginForm definition."""
    # TODO: Define form fields here
    #username
    username = forms.CharField(label="Username", max_length=200, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password
    password = forms.CharField(label="Password", max_length=200, required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserUpdateForm(forms.ModelForm):
    """UserUpdateForm definition."""
    # TODO: Define form fields here
    email = forms.EmailField()
    last_name=forms.CharField(label="Apellidos",max_length=80)
    first_name=forms.CharField(label="Nombres",max_length=80)
    class Meta:
        model=User #USER DE DJANGO
        fields=['last_name','first_name','username','email']

class ProfileUpdateForm(forms.ModelForm):
    image=forms.ImageField(label="Foto de Perfil",widget=forms.FileInput(attrs={'class': 'form-control'}))
    about=forms.CharField(label="Sobre mi",widget=forms.Textarea(attrs={'class': 'form-control',"rows":3}))
    titulo = forms.CharField(label="Especialidad")
    servicios = forms.CharField(help_text="Ingresar valores separado por comas: (Web designer, Fotografo)")
    class Meta:
        model = Profile
        fields=['titulo','phone','image','pais','about','servicios','gitPerfil','linkedPerfil']
