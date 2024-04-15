from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción', null=True)
    precio = models.PositiveIntegerField(default=0)
    cantidad = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    especificaciones = models.TextField(verbose_name='Especificaciones', null=True)

#Editamos los nombres que aparecen en el listado de Libros
    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion + " - " + "Especificaciones: " + self.especificaciones
        return fila
    
    def __int__(self):
        fila = "Precio: " + self.precio + " - " + "Cantidad: " + self.cantidad
        return fila

#Borramos la imagen de la carpeta imagenes al eliminar el registro
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

        