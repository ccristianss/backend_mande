from django.core.validators import RegexValidator
from django.db import models

class Vehicle(models.Model):
    id_vehicle = models.AutoField(primary_key=True)
    user_id_user = models.IntegerField()
    brand_vehicle = models.CharField(max_length=10)
    plate_vehicle = models.CharField(max_length=10)
    model_vehicle = models.DateField(max_length= 4)  # Cambiado a DateField para seleccionar el año
    color_vehicle = models.CharField(max_length=10, validators=[RegexValidator(r'^[a-zA-Z]+$',
                                                                              message='El color solo puede contener letras.')])
    VEHICLE_TYPES = [
        ('Automovil', 'tipo de vehiculo'),
        ('Automovil', 'Automovil'),
        ('Camioneta', 'Camioneta'),
        ('Chana', 'Chana'),
        # Agrega aquí más opciones según sea necesario
    ]
    type_vehicle = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    isverified_vehicle = models.BooleanField(default=False)
    dateregister_vehicle = models.DateTimeField(auto_now_add=True)
    dateupdate_vehicle = models.DateTimeField(auto_now=True)
    dateverified_vehicle = models.DateTimeField(null=True, blank=True)
    image_vehicle = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)

    def __str__(self):
        return self.name_vehicle  # Puedes cambiar esto para mostrar cualquier campo que desees en la representación de cadena del modelo
