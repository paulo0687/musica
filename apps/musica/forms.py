from django import forms
from ckeditor.widgets import CKEditorWidget
from django.core.validators import MinValueValidator
from .models import Comentario, Articulo, Categoria, Contacto

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria', 'user', 'perfil', 'destacado', 'imagen_portada', 'url', 'vistas', 'visible']

    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    contenido = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    destacado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    imagen_portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
    url = forms.SlugField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    vistas = forms.IntegerField(
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    visible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )

class CrearComentarioForm(forms.ModelForm):
    comentario = forms.CharField(
        required=True,
        widget=forms.Textarea()
    )

    class Meta:
        model = Comentario
        fields = ('user', 'perfil', 'comentario', 'articulo')   


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'asunto', 'mensaje')

    nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellido'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    asunto = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'})
    )