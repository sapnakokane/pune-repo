from django import forms
from django.core import validators

class botcls(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    pwd=forms.CharField(widget=forms.PasswordInput)
    repwd = forms.CharField(widget=forms.PasswordInput,label="rpwd")
    bot_handler=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        print("validating fields..")
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['pwd']
        repwd=total_cleaned_data['repwd']
        if pwd != repwd:
            raise forms.ValidationError("password must match..")
        bot_handler=total_cleaned_data['bot_handler']
        if len(bot_handler)>0:
            raise forms.ValidationError("request from BOT.. cannot be submitted")