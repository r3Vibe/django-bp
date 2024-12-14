from django import forms
from unfold.widgets import (
    UnfoldAdminPasswordInput,
    UnfoldAdminSelectWidget,
    UnfoldAdminTextInputWidget,
)
from django.contrib.auth.forms import UserCreationForm
from allauth.socialaccount.admin import SocialAppForm
from allauth.socialaccount import providers


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=UnfoldAdminPasswordInput, label="Password")
    password2 = forms.CharField(
        widget=UnfoldAdminPasswordInput, label="Confirm Password"
    )


class SocialAppFormCustom(SocialAppForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["provider"] = forms.ChoiceField(
            widget=UnfoldAdminSelectWidget, choices=providers.registry.as_choices()
        )
        self.fields["client_id"] = forms.CharField(
            widget=UnfoldAdminTextInputWidget,
        )
        self.fields["key"] = forms.CharField(
            widget=UnfoldAdminTextInputWidget,
        )
        self.fields["secret"] = forms.CharField(
            widget=UnfoldAdminTextInputWidget,
        )
