from django import  forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,label="User name")
    password=forms.CharField(max_length=100,widget=forms.PasswordInput, label="Password")