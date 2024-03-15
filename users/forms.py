from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        Model = User
        fields = ('email', "password1", "password2")


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'telephone_number')


class UserPasswordResetForm(PasswordResetForm):
    pass


class UserSetPasswordForm(SetPasswordForm):
    pass
