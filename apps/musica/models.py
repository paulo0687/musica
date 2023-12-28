from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from apps.users.models import Perfil


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    imagen = models.ImageField(upload_to='musica/categorias/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = RichTextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    imagen_portada = models.ImageField(upload_to='musica/imagenes/', blank=True, null=True)
    destacado = models.BooleanField(default=False)
    url = models.SlugField(max_length=255, unique=True)
    vistas = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('fecha_publicacion',)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.titulo} - {self.user.username}'

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=5000)
    visible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)