from django.db import models

# Create your models here.
class mymodl(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    date=models.DateField()
    # def __str__(self):
    #     return self.name