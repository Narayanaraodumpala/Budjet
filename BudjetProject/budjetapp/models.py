from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Userdetails(models.Model):
    auth_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True,upload_to='media/')
    address=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.auth_user


class Expert(models.Model):

    name=models.CharField(max_length=50,null=True)
    exp_image=models.FileField(null=True,upload_to='experts/')
    description=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name

class Consults(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    exp_image = models.FileField(null=True, upload_to='experts/')
    status=models.CharField(max_length=20,null=True)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

    def __str__(self):

        return self.name



class Slots(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=20, null=True)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Graphs(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=60,null=True)
    value=models.CharField(auto_created=True,max_length=30)

    def __str__(self):

        return self.status
