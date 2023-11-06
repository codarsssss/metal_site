from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from metal_site import settings

from .forms import RegisterUserForm, ProfileUserForm


# Create your views here.
class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")


class ProfileUserView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    extra_context = {
        "title": "Профиль пользователя",
        "default_image": settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
