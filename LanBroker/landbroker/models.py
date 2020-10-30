from django.db import models
from django.contrib.auth.models import AbstractUser, User
from rest_framework.authtoken.models import Token
from django.conf import settings
#from .models import File

class File(models.Model):
    file = models.ImageField(upload_to='landbroker/', default='default.png')
    def __str__(self):
        return self.file.name

# Create your models here.
class profile(models.Model):
    username= models.CharField(max_length=35)
    tel_no = models.CharField(max_length=35)
    photo = models.ImageField(upload_to='photos')
    mob_pswd = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username


class sell(models.Model):
    username= models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    tel_no = models.CharField(max_length=35)
    nin_no= models.CharField(max_length=35)
    reside =models.CharField(max_length=35)
    amount= models.CharField(max_length=35)
    size = models.CharField(max_length=35)
    id_card = models.ImageField(upload_to='landbroker/', default='default.png')
    title_scan = models.ImageField(upload_to='landbroker/', default='default.png')
    map_scan = models.ImageField(upload_to='landbroker/', default='default.png')
    mode_whole= models.BooleanField(default=False)
    mode_part= models.BooleanField(default=False)
    ownership= models.CharField(max_length=35, default='null')
    is_active = models.BooleanField(default=False)
    date_box = models.DateTimeField(auto_now_add=True)
    distance = models.CharField(max_length=35, default='On Road')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.reside

class buy(models.Model):
    username= models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    tel_no= models.CharField(max_length=35)
    reside = models.CharField(max_length=35)
    size= models.CharField(max_length=35)
    amount = models.CharField(max_length=35)
    size_wanted = models.CharField(max_length=35)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.reside
