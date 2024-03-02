from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Requestmanager, Request


@receiver(post_save, sender=Requestmanager)
def update_request_status(sender, instance, created, **kwargs):
    if created:
        # Obtener el objeto Request asociado al Requestmanager
        related_request = instance.request_id_request

        # Actualizar el status_request a 'Proceso'
        related_request.status_request = 'Proceso'
        related_request.save()
