
from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', home_index, name="home"),
]
