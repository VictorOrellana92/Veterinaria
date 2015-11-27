from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, View, TemplateView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascota, Dueno

# Create your views here.

class MostrarMascota(ListView):
	model = Mascota
	template_name = "inicio.html"

mostrar_mascota = MostrarMascota.as_view()

class home(TemplateView): 
	template_name = "login.html"
	success_url = reverse_lazy("mostrar_mascota")

class IngresarMascota(CreateView):
	model = Mascota
	template_name = "mostrar.html"
	fields = "__all__"
	success_url = reverse_lazy("mostrar_mascota")


ingresar_mascota = IngresarMascota.as_view()
