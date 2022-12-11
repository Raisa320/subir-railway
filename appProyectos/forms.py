from django import forms

from appProyectos.models import Proyecto

class ProyectoForm(forms.ModelForm):
    """ProyectoForm definition."""

    # TODO: Define form fields here
    # Título del proyecto
    title = forms.CharField(label="Titulo", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Descripción del proyecto
    descripcion=forms.CharField(label="Descripción",widget=forms.Textarea(attrs={'class': 'form-control',"rows":3}))
    #Tags: HTML, CSS, PYTHON, etc
    tags = forms.CharField(label="Tags",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Foto (que puede ser una URL)
    foto_url = forms.URLField(label="Foto",required=False,widget=forms.URLInput(attrs={'class': 'form-control',"placeholder":"https://..."}))
    foto_img = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control'}))
    #URL de github
    git = forms.URLField(label="Url de Git",widget=forms.URLInput(attrs={'class': 'form-control',"placeholder":"https://..."}))
    #Formulario con validación
    class Meta:
        model=Proyecto #USER DE DJANGO
        fields=['title','descripcion','tags','foto_img','foto_url','git']

    def clean(self):
       cleaned_data = self.cleaned_data
       uploadedfile = cleaned_data.get("foto_img")
       url_address = cleaned_data.get("foto_url")
       
       if not uploadedfile and not url_address :
           raise forms.ValidationError("El campo de foto es obligatorio, ingresa una URL válida o carga una foto")
       return cleaned_data 