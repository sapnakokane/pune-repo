from django.db import models
from django.contrib import admin

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    rollno=models.IntegerField()

    def __str__(self):
        return self.name

class studentAdmin(admin.ModelAdmin):
    list_display=['name','email','address','rollno']

