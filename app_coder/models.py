from django.db import models

# Create your models here.
class Vtuber(models.Model):
    nombre = models.CharField(max_length=40)
    company = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - Compañia: {self.company}"

class User(models.Model):
    nombre = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Username: {self.nombre} #{self.apellido}"

class Moderator(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido} - Profesion: {self.profesion}"

class Post(models.Model):
    nombre =models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    #foto = models.ImageField(upload_to='posts/', null=True, blank=True)
    # La foto es algo a implementar todavia
    def __str__(self):
        return f"Entrega: {self.nombre} / {self.fecha_de_entrega} / {self.entregado}"