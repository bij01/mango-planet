from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=60)
    pwd = forms.CharField(max_length=45)
