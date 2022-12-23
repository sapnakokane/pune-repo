from django.core import validators
from django import forms

#implicit validators or inbuilt validators

def starts_with_s(value):
    if value[0].lower() !='s':
        raise forms.ValidationError("name should strts with s|S ")

class reform(forms.Form):
    name=forms.CharField(validators=[starts_with_s])
    no=forms.IntegerField(min_value=10)
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

# implicit validators using clean method(alterante method)
#
# def clean(self):
#     print("total form validation ")
#     total_cleaned_data=super().clean()
#     inputname=total_cleaned_data['name']
#     if inputname[0].lower()!= 's':
#         raise forms.ValidationError("name should start with s|S ")
#     inputno=total_cleaned_data['no']
#     if inputno<10:
#         raise forms.ValidationError("no should be 10 digit")
