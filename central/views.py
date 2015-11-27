from django.shortcuts import render, redirect
from django.views.generic import (CreateView, DetailView, UpdateView, DeleteView, 
                                  ListView, View, TemplateView, RedirectView)
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Mascota, Dueno, Veterinario

# Create your views here.

class BaseRedirectView(RedirectView):
    permanent = False

    # def dispatch(self, request, *args, **kwargs):
    #     print "hola"
    #     d = super(BaseRedirectView, self).dispatch(request, *args, **kwargs)
    #     user = self.request.user
    #     if user.is_authenticated():
    #         vs = Veterinario.objects.filter(usuario=user)
    #         if vs.exists():
    #             vs = vs.latest('id')
    #             return self.get_redirect_v_url()
    #         else:
    #             ds = Dueno.objects.filter(usuario=user)
    #             if ds.exists():
    #                 ds = ds.latest('pk')
    #                 return self.get_redirect_d_url()
    #     return d

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
        return reverse('ingresar_mascota')

    def get_redirect_d_url(self):
        return reverse('mostrar_mascota')

base_redirect = BaseRedirectView.as_view()

class MostrarMascota(ListView):
    model = Mascota
    template_name = "inicio.html"

mostrar_mascota = MostrarMascota.as_view()

class home(TemplateView): 
    template_name = "login.html"
    success_url = reverse_lazy("mostrar_mascota")

class IngresarMascota(CreateView):
    model = Mascota
    template_name = "nuevamascota.html"
    fields = "__all__"
    success_url = reverse_lazy("mostrar_mascota")


ingresar_mascota = IngresarMascota.as_view()
