from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import (CreateView, DetailView, UpdateView, DeleteView, 
                                  ListView, View, TemplateView, RedirectView)
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Mascota, Dueno, Veterinario, Ficha, Atencion

# Create your views here.

class BaseRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        self.url = '/'
        if user.is_authenticated():
            vs = Veterinario.objects.filter(usuario=user)
            if vs.exists():
                vs = vs.latest('id')
                self.url =  self.get_redirect_v_url()
            else:
                ds = Dueno.objects.filter(usuario=user)
                if ds.exists():
                    ds = ds.latest('pk')
                    self.url = self.get_redirect_d_url()
        print self.url
        return super(BaseRedirectView, self).get(request, *args, **kwargs)


    def get_redirect_v_url(self):
        return reverse('vista_inicio')

    def get_redirect_d_url(self):
        return reverse('vista_inicio')

base_redirect = BaseRedirectView.as_view()

class VistaInicio(ListView):
    model = Mascota
    template_name = "inicio.html"

vista_inicio = VistaInicio.as_view()

class MostrarTodasLasMascotas(ListView): 
    model = Mascota
    template_name = "MostrarTodasLasMascotas.html"
    print Mascota

mostrar_todas_Mascotas = MostrarTodasLasMascotas.as_view()

class MostrarTodasLosDuenos(ListView): 
    model = Dueno
    template_name = "mostrarduenos.html"

mostrar_duenos = MostrarTodasLosDuenos.as_view()

class MostrarTodasLasFichas(ListView): 
    model = Ficha
    template_name = "mostrarFichas.html"

mostrar_fichas = MostrarTodasLasFichas.as_view()

class MostrarTodasLasAtenciones(ListView): 
    model = Atencion
    template_name = "mostrarAtenciones.html"

mostrar_atenciones = MostrarTodasLasAtenciones.as_view()

class MostrarTodosLosVeterinarios(ListView): 
    model = Veterinario
    template_name = "mostrarveterinario.html"

mostrar_veterinarios = MostrarTodosLosVeterinarios.as_view()

class home(TemplateView): 
    template_name = "login.html"
    success_url = reverse_lazy("VistaInicio")

home = home.as_view()

class IngresarMascota(CreateView):
    model = Mascota
    template_name = "nuevamascota.html"
    fields = "__all__"
    success_url = reverse_lazy("mostrar_todas_Mascotas")

ingresar_mascota = IngresarMascota.as_view()

class IngresarDueno(CreateView):
    model = Dueno
    template_name = "nuevoDueno.html"
    fields = "__all__"
    success_url = reverse_lazy("mostrar_duenos")

nuevo_dueno = IngresarDueno.as_view()

class IngresarFicha(CreateView):
    model = Ficha
    template_name = "nuevaFicha.html"
    fields = "__all__"
    success_url = reverse_lazy("mostrar_fichas")

nueva_ficha = IngresarFicha.as_view()

class IngresarAtencion(CreateView):
    model = Atencion
    template_name = "nuevaAtencion.html"
    fields = "__all__"
    success_url = reverse_lazy("mostrar_atenciones")

nueva_atencion = IngresarAtencion.as_view()

class IngresarVeterinario(CreateView):
    model = Veterinario
    template_name = "nuevoveterinario.html"
    fields = "__all__"
    success_url = reverse_lazy("mostrar_veterinarios")

nuevo_veterinario = IngresarVeterinario.as_view()
