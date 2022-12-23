from django.db import models

# Create your models here.
class tempfil(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    date=models.DateField()
    img=models.ImageField()
    sal=models.FloatField()
