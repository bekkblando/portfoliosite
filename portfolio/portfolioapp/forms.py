from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "* Username ↓"
        self.fields['password'].label = "* Password ↓"
        self.fields['email'].label = "* Email Address ↓"
        self.fields['username'].widget.attrs['placeholder'] = "Type Username Here"
        self.fields['password'].widget.attrs['placeholder'] = "Type Password Here"
        self.fields['email'].widget.attrs['placeholder'] = "Type Email Here"

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
