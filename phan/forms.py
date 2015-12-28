from django import forms


class ContactForm(forms.Form):

    """Docstring for . """
    full_name = forms.CharField(max_length=200)
    school = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField()
