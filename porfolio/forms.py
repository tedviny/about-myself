from django import forms
from .models import MessageContact

class ContactForm(forms.Form):
    email = forms.CharField(label="email", max_length=25)
    message = forms.CharField(label="message", max_length=254)
    class Meta:
        model = MessageContact
        fields = '__all__'