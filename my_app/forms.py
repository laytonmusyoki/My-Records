from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Notes

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self,*args,**kwargs):
        super(Registration,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['email'].widget.attrs['placeholder']='email'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='password2'

class Notesform(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['notes']