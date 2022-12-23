from django import forms


class feedback(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()

    def clean(self):
        print("total form validation by using single clean method...")
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if inputname[0].lower()!='p':
            raise forms.ValidationError("name should start with p|P ")
        inputage=total_cleaned_data['age']
        if inputage > 100:
            raise forms.ValidationError("you are not allowed, get lost")

class signupform(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label="reenter password",widget=forms.PasswordInput)
    email=forms.EmailField()

    # def clean(self):
    #     total_cleaned_data=super().clean()
    #     pwd=total_cleaned_data['password']
    #     rpwd=total_cleaned_data['rpassword']
    #     if pwd!=rpwd:
    #         raise forms.ValidationError("password must match")

    def clean_pwd(self):
        pwd=self.cleaned_data['password']
        rpwd=self.cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError("password should match")

