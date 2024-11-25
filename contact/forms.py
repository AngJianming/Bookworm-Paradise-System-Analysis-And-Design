""" File storing form information for contact app """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Data for contact form and widgets to be displayed. """
    class Meta:
        """ Meta class specifying fields and widgets to be displayed. """
        model = Contact
        fields = ('full_name', 'email', 'phone_number', 'message')

    def __init__(self, *args, **kwargs):
        """ Add placeholders / classes / widgets """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True
        self.fields['email'].widget.attrs['class'] = 'emailinput'
