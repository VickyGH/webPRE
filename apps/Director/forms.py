from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm
from django import forms

attrUser = {'class':'form-control'}
attrPass = {}

class MyAuthenticationForm(AuthenticationForm):
    # add your form widget here

    def __init__(self, *args,**kwargs):
        super(MyAuthenticationForm,self).__init__(*args,**kwargs)

        self.base_fields['username'].widget.attrs['class'] = 'form-control'
        self.base_fields['username'].widget.attrs['placeholder'] = 'Usuario'