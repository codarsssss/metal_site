from django.urls import path

from .views import *


app_name = "home_app"

urlpatterns = [
    path("", home_main, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
    path("<slug:slug>", category_detail, name="category_detail"),
]
