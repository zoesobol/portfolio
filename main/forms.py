from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= ["name", "email", "subject", "message"]
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control','name':'name','id':'name', 'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control','name':'email', 'id':'email', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'type': 'text', 'class': 'form-control','name':'subject', 'id':'subject', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','name':'message', 'rows':'5', 'placeholder': 'Your message'}), 
    }
