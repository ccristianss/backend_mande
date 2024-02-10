from django.db import models

# Create your models here.

class Servicios(models.Model):
    id_servicio        = models.AutoField(primary_key=True)
    name_servicio      = models.CharField(max_length=45)
    detail_servicio    = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name_servicios