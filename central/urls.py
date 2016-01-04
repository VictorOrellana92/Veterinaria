from django.conf.urls import url
from . import views
from .views import home

urlpatterns = [
		# url(r'^$',  home.as_view(), name='home'),
		url(r'^$',  'django.contrib.auth.views.login',
		{'template_name': 'login.html'}, name='login'),

		
		url(r'^redirecciona/', views.base_redirect, name = 'base_redirect'),

		url(r'cerrar/$',  'django.contrib.auth.views.logout_then_login', name='logout'),

		url(r'^inicio/$', views.vista_inicio, name = 'vista_inicio'),

		url(r'^nuevamascota/$', views.ingresar_mascota, name = 'ingresar_mascota'),

		url(r'^MostrarTodasLasMascotas/$', views.mostrar_todas_Mascotas, name = 'mostrar_todas_Mascotas'),

		url(r'^nuevamascota/$', views.ingresar_mascota, name = 'ingresar_mascota'),

		url(r'^mostrarduenos/$', views.mostrar_duenos, name = 'mostrar_duenos'),

		url(r'^nuevoDueno/$', views.nuevo_dueno, name = 'nuevo_dueno'),

		url(r'^mostrarFichas/$', views.mostrar_fichas, name = 'mostrar_fichas'),

		url(r'^nuevaFicha/$', views.nueva_ficha, name = 'nueva_ficha'),

		url(r'^mostrarAtenciones/$', views.mostrar_atenciones, name = 'mostrar_atenciones'),

		url(r'^nuevaAtencion/$', views.nueva_atencion, name = 'nueva_atencion'),
		
		url(r'^mostrarveterinario/$', views.mostrar_veterinarios, name = 'mostrar_veterinarios'),

		url(r'^nuevoveterinario/$', views.nuevo_veterinario, name = 'nuevo_veterinario'),

		
]

