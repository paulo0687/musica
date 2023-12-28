from django.contrib import admin
from .models import Categoria, Articulo, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_publicacion', 'categoria', 'user', 'perfil', 'destacado')
    search_fields = ('titulo', 'user__username')  
    prepopulated_fields = {'url': ('titulo',)}  

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'articulo', 'comentario', 'visible')