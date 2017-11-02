from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
	categoria = models.CharField(max_length=100)

	def __str__(self):
		return self.categoria	
	'''class Meta:
		ordering = ['id_categoria']'''		

class Negocio(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=250)
	telefono = models.IntegerField()
	latitud = models.CharField(max_length=100)
	longitud = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria) 

	def __str__(self):
		return self.nombre
			

