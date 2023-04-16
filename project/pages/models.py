import email
from django.db import models

# Create your models here.
class Sign(models.Model):
    Status = (
        ('active' ,'active'),
        ('inactive' ,'inactive'),
    )
    Level =(
        ('first', 'first'),
        ('second', 'second'),
        ('third', 'third'),
        ('fourth', 'fourth'),
    )
    Depart =(
        ('General', 'General'),
        ('Computer Science', 'Computer Science'),
        ('Information System','Information System'),
        ('Information Technology','Information Technology'),
        ('Decision Support','Decision Support'),
        ('Artificial Intelligence','Artificial Intelligence'),
    )
    Gender =(
        ('Male', 'Male'),
        ('Female','Female'),
    )
    name = models.CharField(max_length=50 , null= False)
    id = models.CharField(max_length=60 ,primary_key=True)
    email = models.CharField(max_length=100)
    status =models.CharField(max_length=50 , choices= Status)
    level = models.CharField(max_length=50 ,choices=Level)
    department = models.CharField(max_length= 100 , choices=Depart)
    gpa = models.DecimalField(max_digits= 3 , decimal_places= 2)
    dateOfBirth =models.DateField()
    gender = models.CharField(max_length= 20 ,choices=Gender)
    phone = models.BigIntegerField()
