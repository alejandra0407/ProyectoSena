from django.urls import path
from .views import *

# URLS
urlpatterns = [
#=======================INDEX=====================#
    path('', view_index, name = 'url_index'),
    path('index/', view_index, name = 'url_index'),
#=================================================#

#=======================FICHAS====================#
	path('ficha/index/', view_ficha, name = 'url_fichas'),
#=================================================#

#======================PERMISOS===================#
	path('permiso/index/', view_permiso, name = 'url_permisos'),
#=================================================#

#======================PERSONAS====================#
	path('persona/index/', view_persona, name = 'url_personas'),
#=================================================#

#====================PROGRAMAS====================#
	path('programa/index/', view_programa, name = 'url_programas'),
#=================================================#

#=====================USUARIOS====================#
	path('usuario/index/', view_usuario, name = 'url_usuarios'),
#=================================================#

]
