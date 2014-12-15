from django.db import models

# Create your models here.

class Cuenta (models.Model):
	id_Cuenta = models.AutoField('id_Cuenta', primary_key=True)	
	nombre_cuenta = models.TextField()
	Seguidores = models.IntegerField()
	Siguiendo = models.IntegerField()
	numero_Tweets = models.IntegerField()
	tipo_Cuenta = models.NullBooleanField()
	Sexo = models.NullBooleanField()

	def __unicode__(self):
		return self.nombre_cuenta

class Tweet (models.Model):
	id_Tweet = models.AutoField('id_Tweet', primary_key=True)
	retweet = models.IntegerField()
	favoritos = models.IntegerField()
	tipo_Tweet = models.NullBooleanField()
	id_Cuenta = models.ForeignKey(Cuenta)
	texto = models.TextField()
	fecha = models.DateField() 

	def __unicode__(self):	
		return self.texto
	

class Etiqueta (models.Model):
	id_Etiqueta = models.AutoField('id_Etiqueta', primary_key=True)
	nombre_etiqueta = models.TextField()
	
	def __unicode__(self):
		return self.nombre_etiqueta
	
class Contiene (models.Model):
	id_Tweet = models.ForeignKey(Tweet)
	id_Etiqueta = models.ForeignKey(Etiqueta)

