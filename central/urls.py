from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.mostrar_mascota, name = 'mostrar_mascota'),
]

