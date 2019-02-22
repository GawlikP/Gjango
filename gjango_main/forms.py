from django import forms

class LoginForm(forms.Form):
    name_input = forms.CharField(label='UserName', max_length=100)
    password_input = forms.CharField(label='Passwoed', widget=forms.PasswordInput)

    widgets = {
        'password': forms.PasswordInput()
    }
class RegisterForm(forms.Form):
    name_input = forms.CharField(label='Username', max_length=100)
    password_input = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)
    accept = forms.BooleanField(label='Accept')

    widget = {
        'password': forms.PasswordInput()
    }
