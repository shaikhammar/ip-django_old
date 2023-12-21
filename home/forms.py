from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from users.models import User

class LoginForm(AuthenticationForm):
    username = UsernameField(label='Email address', widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    def confirm_login_allowed(self, user):
        if user.is_staff and not user.is_superuser:
            raise ValidationError(
                ("This account is not allowed here."),
                code='not_allowed',
            )

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')