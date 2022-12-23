from django import forms
from .models import MoviesModel

class DateInput(forms.DateInput):
    input_type = 'date'

class MoviesForm(forms.ModelForm):
    mname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    rdate=forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    hname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    hename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mrating = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model=MoviesModel
        fields='__all__'

