from django import forms


class login_form(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'id': 'username',
            'name': 'username',
            'required': 'required',
            'placeholder': 'Email or Phone Number'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'required': 'required',
            'placeholder': 'Password'
        })
    )
