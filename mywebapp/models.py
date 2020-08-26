from django.db import models

# Create your models here.
class mywebapp(models.Model):
    first_name = models.CharField(max_length= 30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    middleame = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254)
