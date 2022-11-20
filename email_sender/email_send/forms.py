from django import forms
from .models import User


class AddUserForm(forms.ModelForm):
    name = forms.CharField(required=True)
    second_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = '__all__'
