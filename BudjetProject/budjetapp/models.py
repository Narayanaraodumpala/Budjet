from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Userdetails(models.Model):
    auth_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True)
    address=models.CharField(max_length=50,null=True)