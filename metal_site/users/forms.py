import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(
        label="Логин",
        widget=forms.EmailInput(
            attrs={"class": "form-input", "placeholder": "Введите e-mail"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Введите пароль"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password",
        )


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"class": "form-input", "placeholder": "Введите e-mail"}
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Введите пароль"}
        ),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(
            {"class": "form-input", "placeholder": "Повторите пароль"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )
        labels = {
            "email": "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже зарегистрирован!")
        return email


class ProfileUserForm(forms.ModelForm):
    email = forms.CharField(disabled=True, label="E-mail", widget=forms.EmailInput())
    year = datetime.date.today().year
    date_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=tuple(range(year - 100, year - 1)))
    )

    class Meta:
        model = get_user_model()
        fields = (
            "photo",
            "email",
            "first_name",
            "last_name",
            "date_birth",
        )
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
        }
