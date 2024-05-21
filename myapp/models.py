from django.db import models 
from datetime import datetime
# Create your models here.
class details(models.Model):
    name =models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return self.name

