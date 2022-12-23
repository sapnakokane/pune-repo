from django import forms

class additemForm(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()