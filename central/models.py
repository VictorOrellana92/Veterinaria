from django.db import models

# Create your models here.
class Plan(models.Model):
	nombre = models.CharField(max_length=20)
	precio = models.IntegerField()
	estado = models.BooleanField()
	vigencia = models.DurationField()
	capacidad = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class Dueno(models.Model):
	nombre = models.CharField(max_length=20)
	rut = models.CharField(max_length = 9)
	email = models.EmailField()
	direccion = models.CharField(max_length = 100)
	comuna = models.CharField(max_length = 30)
	phone = models.CharField(max_length=20)
	usuario = models.CharField(max_length=20)
	contrasena = models.CharField(max_length=20)
	Tipo_Usuario = (
			('C', 'Cliente'),
			('V', 'Veterinario'),
			('A', 'Administrador'),
		)
	Tipo_de_Usuario = models.CharField(max_length=1, choices=Tipo_Usuario)

	def __unicode__(self):
		return self.nombre

class Mascota(models.Model):
	nombre = models.CharField(max_length=20)
	dueno = models.ForeignKey('Dueno')
	sexo = models.CharField(max_length=10)
	fecha_nacimiento = models.DateField()
	observaciones = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class Clinica(models.Model):
	#id
	rut = models.CharField(max_length = 9)
	nombre = models.CharField(max_length = 20)
	email = models.EmailField()
	direccion = models.CharField(max_length = 100)
	comuna = models.CharField(max_length = 30)
	phone = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class OrdenCompra(models.Model):
	clinica = models.ForeignKey('Clinica')
	plan = models.ForeignKey('Plan')
	inicio = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.plan

class HistorialCompra(models.Model):
	numero_compra = models.ForeignKey('OrdenCompra')

	def __unicode__(self):
		return self.numero_compra

class Veterinario(models.Model):
	nombre = models.CharField(max_length = 20)
	especialidad = models.CharField(max_length = 30)
	usuario = models.CharField(max_length=20)
	contrasena = models.CharField(max_length=20)
	Tipo_de_Usuario = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre


class Ficha(models.Model):
	nombre = models.ForeignKey('Mascota')
	clinica = models.ForeignKey('Clinica')
	amo = models.ForeignKey('Dueno')
	creacion = models.DateField(auto_now=True)

	def __unicode__(self):
		return unicode(self.nombre)

class Atencion(models.Model):
	ficha = models.ForeignKey('Ficha')
	domicilio = models.BooleanField()
	fecha_Atencion = models.DateField()
	veterinario = models.ForeignKey('Veterinario')
	temperatura = models.FloatField()
	observaciones = models.TextField()
	diagnostico = models.CharField(max_length=20)

	def __unicode__(self):
		return self.ficha