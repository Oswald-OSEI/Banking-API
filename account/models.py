from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import manager

# Create your models here.
def user_profile_pics_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/passport_pics/{0}'.format(filename)
class Account(AbstractUser):
    username = None
    email = models.EmailField(null = True, unique = True)
    first_name = models.CharField(max_length = 200 )
    last_name = models.CharField(max_length = 200)
    telephone_number= models.CharField(max_length = 10, null=True)
    passport_picture = models.ImageField(upload_to= user_profile_pics_directory)
    gender_choices = (
        ("M", "MALE"), 
        ("F", "FEMALE"),
    )
    Gender = models.CharField(max_length = 1, choices = gender_choices, null = True)
    date_of_birth = models.DateField(null=True, blank=True)
    national_id_type = (
        ('Ghana Card', "Ghana Card"), 
        ('Passport', "Passport"), 
        ("Driver License", "Driver license"),
    )
    Id_type = models.CharField(max_length = 30, choices = national_id_type)
    Id_number = models.CharField(max_length = 20)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "telephone_number"]
    objects = manager()



class loginmodel(models.Model):
    email = models.EmailField()
    

    
    
    