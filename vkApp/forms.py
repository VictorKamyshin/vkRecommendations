from django import forms
from django.contrib.auth.models import User


class AuthorisationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby': 'basic-addon1', 'placeholder': 'Alex',
                                                             'class': 'form-control'}), label=u'Username',
                               required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'aria-describedby': "basic-addon1",
                                                                  'placeholder': "qwer1234", 'class': "form-control"}),
                                label=u'Password', required=True)
