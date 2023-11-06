from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import *


app_name = "users"

urlpatterns = [
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("profile/", ProfileUserView.as_view(), name="profile"),
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
            extra_context={"title": "Сброс пароля!"},
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html",
            extra_context={"title": "Сброс пароля!"},
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            extra_context={"title": "Восстановление пароля"},
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
            extra_context={"title": "Пароль восстановлен"},
        ),
        name="password_reset_complete",
    ),
]
