from django.forms import Form
from django import forms

gender=(
    ('male','male'),
    ('female','female'),
    ('other','other'),

)
class myform(Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    date=forms.DateField()
    gender=forms.ChoiceField(choices=gender)

class myform1(Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    date=forms.DateField()
    img=forms.ImageField()
    feedback=forms.CharField(widget=forms.Textarea)
