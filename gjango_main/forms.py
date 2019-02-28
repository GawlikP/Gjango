from django import forms

CLASSES_CHOICES = (
    (1, ("Warrior")),
    (2, ("Barbarian")),
    (3, ("Mage")),
    (4, ("Thief")),
    (5, ("Monk"))
)

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

class CreatePlayerForm(forms.Form):
    name_input = forms.CharField(label='Characher name', max_length=100)
    Type_choice = forms.ChoiceField(choices=CLASSES_CHOICES,required=True)
