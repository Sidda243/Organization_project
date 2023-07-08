from app.models import * 
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        # widgets = {'password' : forms.PasswordInput,
        #'username':forms.TextInput(attrs = {'class':'form-control'}),
        # 'email':forms.TextInput(attrs = {'class':'form-control'}),
        # }
        help_texts = {'username' : ""}


class OrganizationForm(forms.ModelForm):
    username = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)

    class Meta:
        model = Organization
        fields = '__all__'