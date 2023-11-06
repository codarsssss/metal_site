from django.urls import path

from .views import *


app_name = "home_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", about, name="about"),
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("<slug:slug>", category_detail, name="category_detail"),
]
