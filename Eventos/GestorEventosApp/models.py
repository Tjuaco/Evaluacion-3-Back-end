# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Categoria'


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Evento'


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'Ubicacion'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Usuario'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
