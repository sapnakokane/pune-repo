from django import forms

class cform(forms.Form):
    name=forms.CharField()
    date=forms.DateField()