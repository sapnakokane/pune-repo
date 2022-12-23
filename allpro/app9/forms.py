from django import forms
from app9.models import smodl

class smodlForm(forms.ModelForm):
    class Meta:
        model=smodl
        fields='__all__'
        # fields=('field1','field2','field3')  To include fields
        # exclude=['field2','field3']    To exclude fields
