from __future__ import annotations
from typing import TYPE_CHECKING
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm

if TYPE_CHECKING:
    from django.http import HttpRequest


@login_required
def dashboard(request: HttpRequest):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def user_login(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfuly')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
