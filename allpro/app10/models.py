from django.db import models
from django import forms
# Create your models here.


class MoviesModel(models.Model):
    mname=forms.CharField(max_length=30)
    rdate=forms.DateField()
    hname=forms.CharField(max_length=30)
    hename = forms.CharField(max_length=30)
    dname = forms.CharField(max_length=30)
    mrating = forms.CharField(max_length=30)