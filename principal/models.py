from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Medico(models.Model):
    idMedico=models.IntegerField(primary_key=True)
    nombreMedico=models.CharField(max_length=50)
    apellidoMedico=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=50)

     

class UsuarioP3(models.Model):
    rut=models.CharField(max_length=30, primary_key=True)
    email=models.CharField(max_length=300)
    nombre=models.CharField(max_length=300)
    edad=models.CharField(max_length=300)
    password=models.CharField(max_length=10)   

class UsuarioM(models.Model):
    id=models.CharField(max_length=30, primary_key=True)
    nombre=models.CharField(max_length=300)
    password=models.CharField(max_length=10)

class UsuarioS(models.Model):
    id=models.CharField(max_length=30, primary_key=True)
    nombre=models.CharField(max_length=300)
    password=models.CharField(max_length=10)        

class Dia(models.Model):
    dia=models.CharField(max_length=20)  

class Mes(models.Model):
    mes=models.CharField(max_length=30)    

class Hora(models.Model):
    hora=models.CharField(max_length=50)

class Agendar(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.ForeignKey(Dia, on_delete=models.CASCADE)
    mes=models.ForeignKey(Mes, on_delete=models.CASCADE)
    hora=models.ForeignKey(Hora, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
        