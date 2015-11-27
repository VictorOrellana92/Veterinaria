from django.contrib import admin
from .models import Plan,Dueno,Mascota,Clinica,OrdenCompra,HistorialCompra,Veterinario,Ficha,Atencion

# Register your models here.

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'precio', 'estado', 'vigencia', 'capacidad']

@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'rut', 'email', 'direccion', 'comuna', 'phone', 'usuario']

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'dueno', 'sexo', 'fecha_nacimiento', 'observaciones']

@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
	list_display = ['rut', 'nombre', 'email', 'direccion', 'comuna', 'phone']

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
	list_display = ['clinica', 'plan', 'inicio']

@admin.register(HistorialCompra)
class HistorialCompraAdmin(admin.ModelAdmin):
	list_display = ['numero_compra']

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'especialidad', 'usuario', 'Tipo_de_Usuario']

@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'clinica', 'amo', 'creacion']

@admin.register(Atencion)
class AtencionpsAdmin(admin.ModelAdmin):
	list_display = ['ficha', 'domicilio', 'fecha_Atencion', 'veterinario', 'temperatura', 'observaciones', 'diagnostico']