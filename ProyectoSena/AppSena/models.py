from django.db import models
from django.contrib.auth.models import User

# MODELS
#======================PERMISO====================#
class Permiso(models.Model):
	motivos = (
		('Enfermedad', 'Enfermedad'),
		('Accidente', 'Accidente'),
		('Calamidad domestica', 'Calamidad domestica'),
		('Otro','Otro'),
		)
	motivo = models.CharField(max_length = 45,  choices=motivos)
	solicitoPermisoPor = models.CharField(max_length = 300, null = True, blank=True)
	permisoPorHora =  models.CharField(max_length = 45, null = True, blank=True)
	permisoPorDias = models.CharField(max_length = 45, null = True, blank=True)
	horaSalida = models.CharField(max_length = 45)
	fecha = models.DateField()

	def __str__(self):
		return self.horaSalida
#=================================================#

"""#======================USUARIO====================#
class Usuario(models.Model):
	nombreUsuario = models.CharField(max_length = 45, unique = True)
	email = models.EmailField(max_length = 50, unique = True)
	contraseña = models.CharField(max_length = 45)
	def __str__(self):
		return self.nombreUsuario
#=================================================#"""

#======================PERSONA====================#
class Persona(models.Model):
	documentoIdentidad = models.CharField(max_length = 20, unique = True)
	primerNombre = models.CharField(max_length = 45)
	segundoNombre = models.CharField(max_length = 45, null = True, blank = True)
	primerApellido = models.CharField(max_length = 45)
	segundoApellido = models.CharField(max_length = 45, null = True, blank = True)
	contacto = models.CharField(max_length = 10)
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.primerNombre
#=================================================#

#==================PERSONA=PERMISO================#
class Permiso_persona(models.Model):
	est = (
			('En Espera', 'En Espera'),
			('Aprobado','Aprobado'),
			('Cancelado','Cancelado'), 
			('Rechazado','Rechazado'),
			('Finalizado','Finalizado'),
		)
	estado = models.CharField(max_length = 20,  choices=est)
	instructor = models.CharField(max_length = 100, null = True, blank=True)
	vigilante = models.CharField(max_length = 100, null = True, blank=True)
	permiso = models.ForeignKey(Permiso, on_delete = models.CASCADE)
	persona = models.ForeignKey(Persona, on_delete = models.CASCADE)

	def __str__(self):
		return self.persona.primerNombre
#=================================================#

#=======================ROL=======================#
class Rol(models.Model):
	rol = models.CharField(max_length = 20)

	def __str__(self):
		return self.rol
#=================================================#

#====================ROL=PERSONA==================#
class Rol_persona(models.Model):
	rol = models.ForeignKey(Rol, on_delete = models.CASCADE)
	persona = models.ForeignKey(Persona, on_delete = models.CASCADE)


	def __str__(self):
		return self.rol.rol+'_'+self.persona.primerNombre
#=================================================#

#=====================PROGRAMA====================#
class Programa(models.Model):
	nombre = models.CharField(max_length = 100)
	codigoPrograma = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre
#=================================================#

#======================FICHA======================#
class Ficha(models.Model):
	jornadas = (
		('Mañana', 'Mañana'),
		('Tarde', 'Tarde'),
		('Noche', 'Noche'),
		)
	numeroFicha = models.CharField(max_length = 20, unique = True)
	jornada = models.CharField(max_length = 20, choices = jornadas)
	ambiente = models.CharField(max_length = 50)
	lider = models.CharField(max_length = 100)
	fechaFinEtapaLectiva = models.DateField()
	programa = models.ForeignKey(Programa, on_delete = models.CASCADE)

	def __str__(self):
		return self.numeroFicha+' _ '+self.programa.nombre
#=================================================#

#===================PERSONA=FICHA=================#
class Persona_ficha(models.Model):
	persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
	ficha = models.ForeignKey(Ficha, on_delete = models.CASCADE)
	programa = models.ForeignKey(Programa, on_delete = models.CASCADE)

	def __str__(self):
		return self.persona.primerNombre+'_'+self.ficha.numeroFicha+'_'+self.programa.nombre
#=================================================#