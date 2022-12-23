from django import forms
from app4.models import SapModel

class SapForm(forms.ModelForm):
    class Meta:
        model=SapModel
        fields='__all__'




