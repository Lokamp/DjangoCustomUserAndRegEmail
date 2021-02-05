from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import DefaultUser, CompanyUser


class RegistrationUserFirstForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = DefaultUser
        fields = ('email',)


class RegistrationUserSecondForm(forms.ModelForm):

    class Meta:
        model = CompanyUser
        fields = ('first_name', 'last_name')




