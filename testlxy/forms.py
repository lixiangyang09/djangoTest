from django import forms

class AddForm(forms.Form):
    name = forms.CharField(max_length=200)
    passwd = forms.CharField(max_length=200)
