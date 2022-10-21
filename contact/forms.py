from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact form for users to contact customer support """
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'subject', 'message')

    # first_name = forms.CharField(max_length=55, required=True)
    # last_name = forms.CharField(max_length=55, required=True)
    # email = forms.EmailField(max_length=254, required=True)
    # subject = forms.CharField(max_length=55, required=True)
    # message = forms.CharField(widget=forms.Textarea, required=True,
    #                           max_length=1000)
