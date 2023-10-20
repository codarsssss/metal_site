from django import forms
from django.core.validators import RegexValidator

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        label="Ваше имя",
        max_length=64,
        min_length=2,
        widget=forms.TextInput(
            attrs={"placeholder": "Ваше имя"},
        ),
    )
    email = forms.EmailField(
        label="Электронная почта (email)",
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "E-mail"}),
    )
    contact_number = forms.SlugField(label="Номер телефона")
    comment = forms.CharField(
        label="Текст сообщения",
        widget=forms.Textarea(
            attrs={"placeholder": "Ваше сообщение", "cols": 30, "rows": 9}
        ),
    )

    class Meta:
        model = Feedback
        fields = ("name", "email", "contact_number", "comment")
