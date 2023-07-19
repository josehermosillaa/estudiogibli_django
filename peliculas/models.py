from django.db import models

# Create your models here.

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True) # 1 2 3 ... etc uuidField (campoaleatorio)
    title = models.CharField(max_length=255, verbose_name="Titulo") #alfanumericos -> str
    poster = models.URLField(max_length=255, verbose_name="Poster")
    genre = models.CharField(max_length=255, verbose_name="Genero")
    rating = models.CharField(max_length=255,  verbose_name="Clasificacion")
    release = models.DateTimeField(blank=True, null=True,verbose_name="Lanzamiento")
    director = models.CharField(max_length=255, verbose_name="Director")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    class Meta :
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"
        ordering = ("-created",)

    def __str__(self):
        return self.title
    