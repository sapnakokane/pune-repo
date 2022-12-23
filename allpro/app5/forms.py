from django import forms

class formex(forms.Form):
    name=forms.CharField()  #max_length not recommanded
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        print("validating name")
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("max len should be > 4 ")
        return inputname + 'kokane'
    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print("validating roll no")
        return inputrollno
    def _clean_email(self):
        inputemail=self.cleaned_data['email']
        print("validating email field")
        return inputemail
    def clean_feedbackform(self):
        inputfeedback=self.cleaned_data['feedback']
        print("validating feedback input")
        return inputfeedback

