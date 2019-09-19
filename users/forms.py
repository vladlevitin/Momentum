from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User, Startup, Investor, Person
from django.db import transaction
import googlemaps
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class StartupRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_startup = True
        user.save()
        return user


class InvestorRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_investor = True
        user.save()
        return user


class PersonRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_person = True
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class StartupUpdateForm(forms.ModelForm):

    class Meta:
        model = Startup

        gmaps = googlemaps.Client(key='AIzaSyAJ1Pg7lnVTZrd8YUJQHrmlPQCD49IfWIs')
        gmaps.geocode(Startup.address)

        fields = ['name', 'address', 'latitude', 'longitude', 'startup_link', 'sector',
                  'industry', 'status', 'ceo', 'employees', 'bio', 'image']


class InvestorUpdateForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['name', 'email2', 'address', 'latitude', 'longitude', 'investor_link', 'status_interest', 'bio', 'image']


class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'address', 'birthday', 'occupation', 'bio', 'image',
                  'edu_started', 'edu_ended', 'edu_location', 'edu_type', 'edu_title',
                 'work_employer', 'work_position', 'work_type', 'work_description']
