from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate
from . import forms

def login_page(request):
    form=forms.LoginForm()
    message='foo'
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']

            )
        if user is not None:
            login(request,user)
            message=f'Please come in '
        else:
            message='No Way'
    return render(request,'authentication/login.html',context={'form': form, 'message': message})


