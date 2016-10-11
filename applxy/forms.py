#forms

from django import forms
from .models import *

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


class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    ffff = forms.ModelChoiceField(queryset=Product.objects.all(),
                                  widget=forms.RadioSelect())

class FormProduct2(forms.Form):
    ffff = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.RadioSelect(), empty_label=None)
