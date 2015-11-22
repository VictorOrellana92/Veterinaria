from django.conf.urls import url
from . import views
from .views import home

urlpatterns = [
		url(r'^$',  home.as_view(), name='home'),
		url(r'^mascotas/$', views.mostrar_mascota, name = 'mostrar_mascota'),
		
]

