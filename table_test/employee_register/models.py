from django.db import models

# Create your models here.

class Employee(models.Model):
    seu_codigo = models.CharField(max_length=100)
    
