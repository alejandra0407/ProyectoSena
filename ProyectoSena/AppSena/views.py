from django.shortcuts import render
from .models import *

# VIEWS
#=======================INDEX=====================#
def view_index(request):
	return render(request, 'index.html')
#=================================================#

#=======================FICHA=====================#
def view_ficha(request):
	ficha = Ficha.objects.all()
	return render(request, 'ficha/index.html', locals())
#=================================================#

#=====================PERMISO=====================#
def view_permiso(request):
	permiso = Permiso.objects.all()
	return render(request, 'permiso/index.html', locals())
#=================================================#

#=====================PERSONA=====================#
def view_persona(request):
	persona = Persona.objects.all()
	return render(request, 'persona/index.html', locals())
#=================================================#

#====================PROGRAMA=====================#
def view_programa(request):
	programa = Programa.objects.all()
	return render(request, 'programa/index.html', locals())
#=================================================#

#=====================USUARIO=====================#
def view_usuario(request):
	usuario = User.objects.all()
	return render(request, 'usuario/index.html', locals())
#=================================================#