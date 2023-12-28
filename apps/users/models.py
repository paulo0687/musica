# en apps/users/models.py

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    imagen = models.ImageField(
        upload_to='users/imagenes',
        default='users/imagenes/users.jpg'
    )
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username 



