from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from unicodedata import name
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=6 ,decimal_places=3)
    image = models.ImageField(upload_to ='photos/%y/%m/%d' ,null = True, default ='photos\22\05\19.png')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

    class Meta :
        verbose_name = 'phone' 
    class Meta :
        ordering = ['price']       