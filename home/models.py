from dataclasses import fields
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    desc=models.TextField(null=True)
    date=models.DateField(null=True)
    
    def __str__(self):
        return self.name