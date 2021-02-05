from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .forms import (
    RegistrationUserFirstForm,
    RegistrationUserSecondForm
)
from .models import DefaultUser, CompanyUser


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


def registration_company_view(request):
    """Регистрация компанни. Передается две формы для заполнения двух моделей
   DefaultUser и CompanyUser"""

    form_default_user = RegistrationUserFirstForm()
    form_company = RegistrationUserSecondForm()
    if request.user.is_authenticated:
        return redirect('home')
    if request.POST:
        form_default_user = RegistrationUserFirstForm(request.POST)
        form_company = RegistrationUserSecondForm(request.POST)
        if form_default_user.is_valid() and form_company.is_valid():
            email = form_default_user.cleaned_data['email']
            raw_pass = form_default_user.cleaned_data.get('password1')
            first_name = form_company.cleaned_data['first_name']
            last_name = form_company.cleaned_data['last_name']
            user = DefaultUser.objects.create_user(email=email, password=raw_pass)
            company_user = CompanyUser(first_name=first_name, last_name=last_name, user=user)
            company_user.save()
            user_auth = authenticate(
                email=email,
                password=raw_pass,
            )
            login(request, user)
            return redirect('home')
    context = {
        'form_default_user': form_default_user,
        'form_company': form_company
    }
    return render(request, 'registration.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('home')
