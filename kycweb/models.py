from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.db.models.signals import post_save
class Profile(models.Model):
    filetype=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='picture' , blank=True)
