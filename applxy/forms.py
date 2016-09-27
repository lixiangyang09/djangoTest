#forms

from django import forms


class EmptyForm(forms.Form):
    pass


class FormLogin(forms.Form):
    name = forms.CharField(max_length=200)
    passwd = forms.CharField(max_length=200)


class FormChangePasswd(forms.Form):
    new = forms.CharField(max_length=200)
    confirm = forms.CharField(max_length=200)


class FormRegister(forms.Form):
    name = forms.CharField(max_length=200)
    passwd = forms.CharField(max_length=200)
    confirm = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)

