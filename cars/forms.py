from django import forms
from .models import NewUser
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'user_email', 'user_phone', 'user_age_month', 'user_age_day', 'user_age_year', 'user_country']


class FinalizeUserForm(forms.ModelForm):
    user_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text="6-10 characters. Must include 1 number, 1 special char, no char repeated >2 times."
    )

    class Meta:
        model = NewUser
        fields = ['user_nickname', 'user_password']

    def clean_user_nickname(self):
        nickname = self.cleaned_data.get('user_nickname')
        if NewUser.objects.exclude(id=self.instance.id).filter(user_nickname=nickname).exists():
            raise ValidationError("This nickname is already taken.")
        return nickname

    def clean_user_password(self):
        password = self.cleaned_data.get('user_password')

        if len(password) < 6 or len(password) > 10:
            raise ValidationError("Password must be between 6 and 10 characters.")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_password = self.cleaned_data['user_password']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    user_nickname = forms.CharField(max_length=15, required=True)
    user_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        nickname = cleaned_data.get("user_nickname")
        password = cleaned_data.get("user_password")

        if nickname and password:
            try:
                user = NewUser.objects.get(user_nickname=nickname)
                if user.user_password != password:
                    raise ValidationError("Incorrect password.")
            except NewUser.DoesNotExist:
                raise ValidationError("User with this nickname does not exist.")
        return cleaned_data
