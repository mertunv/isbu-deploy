from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Profile, Invitation


class AccountRegistrationForm(UserCreationForm):
    CHOICE = [
        ('is_employee', 'Employee'),
        ('is_employer', 'Employer')
    ]

    userTypes = forms.CharField(label = 'User Type', widget = forms.RadioSelect(choices = CHOICE))

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name']


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        exclude = ('user',)

        widgets = {
            'dob': forms.DateInput(attrs = {'type': 'date'})
        }


class EmployeeInvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation

        widgets = {
            "date": forms.DateInput(attrs = {"type": "date"})
        }

        fields = ["date", "message"]