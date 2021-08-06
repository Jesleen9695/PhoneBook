from django import forms
from . import models

class AddContact(forms.ModelForm):
    class Meta:
        model = models.Contacts
        fields = ['first_name', 'last_name', 'phone', 'email_addr', 'street_addr']