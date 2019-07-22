from django import forms

class UserCreateForm(forms.Form):
	Email = forms.EmailField(max_length=100)
	Password = forms.CharField(max_length=100, widget=forms.PasswordInput)
