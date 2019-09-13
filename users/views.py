from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import Register, LoginForm



from django.contrib.auth import authenticate, login, logout

def register(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:list'))

    form = Register(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        authuser = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if authuser:
            login(request,user)
            return HttpResponseRedirect(reverse('app:list'))
    return render(request,'register.html',context={'form':form})



def user_login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:list'))

    form = LoginForm(request.POST or None)
    if form.is_valid():
        authuser = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if authuser:
            login(request, authuser)
            return HttpResponseRedirect(reverse('app:list'))
    return render(request, 'login.html', context={'form': form})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:list'))