from django.db import models

# Create your models here.
class Persona(models.Model):

    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s" % (self.nombres, self.apellidos, self.cedula)

class Barrio(models.Model):

    nombres = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (self.nombres, self.siglas)

class Casa(models.Model):

    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="casas")
    direccion = models.CharField(max_length=30)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="casas")
    valor = models.IntegerField()
    color = models.CharField(max_length=30)
    num_cuartos = models.IntegerField()
    num_pisos = models.IntegerField()

    def __str__(self):
        return "%s - %s - %s - %s - %s - %s - %s" % (self.propietario, \
        self.direccion, self.barrio, self.valor, self.color ,self.num_cuartos, \
        self.num_pisos)

class Departamento(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="departamentos")
    direccion = models.CharField(max_length=30)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="casas")
    valor = models.IntegerField()
    num_cuartos = models.IntegerField()
    costo_mensual = models.DecimalField(max_digits=65, decimal_places=2)

    def __str__(self):
        return "%s - %s - %s - %s - %s - %s" % (self.propietario, \
        self.direccion, self.barrio, self.valor ,self.num_cuartos, \
        self.costo_mensual)
