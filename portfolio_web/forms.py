from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    phone = forms.CharField(max_length=13)
    content = forms.CharField(widget=forms.Textarea, max_length=400)