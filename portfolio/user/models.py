from django.db import models

# Create your models here.

class details(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    contact_no=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    message=models.CharField(max_length=90)
