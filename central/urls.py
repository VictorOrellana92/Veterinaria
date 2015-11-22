from django.conf.urls import url
from . import views
from .views import home

urlpatterns = [
		url(r'^$',  home.as_view(), name='home'),
		url(r'^vermascota/$', views.mostrar_mascota, name = 'mostrar_mascota'),
		url(r'^nuevamascota/$', views.ingresar_mascota, name = 'ingresar_mascota'),

		
]

