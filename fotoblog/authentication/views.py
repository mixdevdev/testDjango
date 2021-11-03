from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
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
            message=f"welcome {user.username} with password {user.password}"
        else:
            message='No Way'
    return render(request,'authentication/login.html',context={'form': form, 'message': message})


def logout_page(request):
    logout(request)
    return redirect('login')