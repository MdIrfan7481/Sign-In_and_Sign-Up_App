from django.db import models

class Reg(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=10)
    Cpassword= models.CharField(max_length=10)
    MobileNumber = models.IntegerField()
    Emailid =models.EmailField()
