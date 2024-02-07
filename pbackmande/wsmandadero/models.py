from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class Account_User(models.Model):
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
    
class Mandadero(models.Model):
    id_Mandadero              = models.AutoField(primary_key=True)
    id_Account_User_Mandadero = models.ForeignKey('Account_User', on_delete=models.CASCADE)
    name_Mandadero            = models.CharField(max_length=45)
    lastName_Mandadero        = models.CharField(max_length=45)
    phone_Mandadero           = models.CharField(max_length=10)
    image_Mandadero           = models.ImageField (upload_to='imgMandadero',max_length=255)
    ishavecar_Mandadero       = models.BooleanField()
    ishavemoto_Mandadero      = models.BooleanField()
    isactive_Mandadero        = models.BooleanField(default=True)
    isvalidate_Mandadero      = models.BooleanField(default=True)
    dateregister_Mandadero    = models.DateTimeField(auto_now_add=True)
    dateupdate_Mandadero      = models.DateTimeField(auto_now=True)
    address_Mandadero         = models.CharField(max_length=100)
    cc_Mandadero              = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.name_Mandadero