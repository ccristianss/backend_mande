from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Account(models.Model):
    id_Acount_User            = models.AutoField(primary_key=True)
    email_Account_User        = models.EmailField(max_length=45, unique=True)
    password_Account_User     = models.CharField(max_length=255)
    dateregister_Account_User = models.DateField(auto_now_add=True)
    dateupdate_Account_User   = models.DateField(auto_now=True)
    isadmin_Acount_User       = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        
        if not self.password_Account_User.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2$')):
            self.password_Account_User = make_password(self.password_Account_User)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email_Account_User
    
    class Meta:
        db_table = 'account'

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account_id_account', unique=True)  
    name_user = models.CharField(max_length=45)
    lastname_user = models.CharField(max_length=45)
    phone_user = models.CharField(max_length=10)
    dateregister_user = models.DateTimeField(auto_now_add=True)
    dateupdate_user = models.DateTimeField(auto_now=True)
    ismander_user = models.BooleanField(default=False) 
    image_user = models.ImageField(upload_to='users', null=True)

    class Meta:
        db_table = 'user'

class Mander(models.Model):
    id_mander = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id_user')
    ishavecar_mander = models.BooleanField()
    ishavemoto_mander = models.BooleanField()
    isactive_mander = models.BooleanField(default=False)
    isvalidate_mander = models.BooleanField(default=False)
    dateregister_mander = models.DateTimeField(auto_now_add=True)
    dateupdate_mander = models.DateTimeField(auto_now=True) 
    address_mander = models.CharField(max_length=100)
    cc_mander = models.CharField(max_length=13)  
    image_mander = models.ImageField(upload_to='manders', null=True)

    def __str__(self) -> str:
        return self.name_Mandadero

    class Meta:
        db_table = 'mander'

class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id_user')
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