from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact form for users to contact customer support """
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'subject', 'message')
