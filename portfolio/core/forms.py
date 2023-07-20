from django import forms
from django.core.validators import EmailValidator
from .models import *


class CVUploadForm(forms.Form):
    cv = forms.FileField(label='CV', widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)

class ContactForm(forms.Form):

    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', validators=[EmailValidator()], max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']