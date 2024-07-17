from django.db import models

class Edificio(models.Model):
    TIPOS_CIUDAD = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices= TIPOS_CIUDAD)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.get_tipo_display())

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=0)
    nCuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="edificio_departamento")

    def __str__(self):
        return "%s %s %s" % (self.nombre, 
                self.costo, 
                self.nCuartos)