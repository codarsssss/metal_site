from django import forms
from captcha.fields import CaptchaField


from .models import Feedback


class FeedbackForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = (
            "name",
            "email",
            "contact_number",
            "comment",
            "captcha",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ваше имя"}
            ),
            "email": forms.EmailInput(attrs={"placeholder": "E-mail"}),
            "contact_number": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Номер телефона"}
            ),
            "comment": forms.Textarea(
                attrs={"placeholder": "Ваше сообщение", "cols": 25, "rows": 9}
            ),
        }

    def clean_contact_number(self):
        contact_number = self.cleaned_data["contact_number"]
        allowed = "+1234567890"
        if not (set(contact_number) <= set(allowed)):
            raise forms.ValidationError(
                "Телефонный номер содержим недопустимые символы (формат '+79999999999')"
            )
        if not (10 < len(contact_number) <= 12):
            raise forms.ValidationError(
                "Введите корректное значение телефонного номера в формате '+79999999999'"
            )
        return contact_number
