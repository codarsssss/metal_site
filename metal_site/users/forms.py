import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Введите логин"}
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
            "username",
            "password",
        )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Введите логин"}
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
            "username",
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
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Введите адрес email"}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже зарегистрирован!")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label="Логин", widget=forms.TextInput())
    email = forms.CharField(disabled=True, label="E-mail", widget=forms.EmailInput())
    year = datetime.date.today().year
    date_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=tuple(range(year - 100, year - 1)))
    )

    class Meta:
        model = get_user_model()
        fields = (
            "photo",
            "username",
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
