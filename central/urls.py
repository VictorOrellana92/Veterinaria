from django.conf.urls import url
from . import views
from .views import home

urlpatterns = [
		# url(r'^$',  home.as_view(), name='home'),
		url(r'^$',  'django.contrib.auth.views.login',
		{'template_name': 'login.html'}, name='login'),

		url(r'cerrar/$',  'django.contrib.auth.views.logout_then_login', name='logout'),

		url(r'^inicio/$', views.mostrar_mascota, name = 'mostrar_mascota'),

		url(r'^nuevamascota/$', views.ingresar_mascota, name = 'ingresar_mascota'),

		
]

