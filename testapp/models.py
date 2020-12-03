from django.db import models

# Create your models here.
class Prod(models.Model):
	prodname=models.CharField(max_length=255)
	prodprice=models.FloatField()
	prodimage=models.ImageField(upload_to='uploads/')
	prodimage1=models.ImageField(upload_to='uploads/')
	proddesc=models.TextField()