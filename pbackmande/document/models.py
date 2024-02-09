from django.db import models

# Create your models here.
class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    #user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_user')
    user = models.IntegerField()
    url_document = models.CharField(max_length=255) 
    isdocument_vehicle = models.BooleanField()
    isverified_document = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('CC', 'CC'),
        ('SOAT', 'SOAT'), 
        ('LICENCIA', 'LICENCIA'),
        ('OPERACION', 'OPERACION'), 
        ('TECNOMECANICA', 'TECNOMECANICA'),
        ('RECIBO', 'RECIBO')
    )
    type_document = models.CharField(max_length=15, choices=TYPE_CHOICES) 
    dateregister_document = models.DateTimeField(auto_now_add=True)
    dateupdate_document = models.DateTimeField(auto_now=True)
    dateverified_document = models.DateTimeField(null=True) 

    class Meta:
        db_table = 'document'
