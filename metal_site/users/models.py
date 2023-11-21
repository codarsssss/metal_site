from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    email = models.EmailField(max_length=128, unique=True, verbose_name="E-mail адрес")
    photo = models.ImageField(
        upload_to="users/%Y",
        blank=True,
        null=True,
        verbose_name="Фотография",
        default="default.png",
    )
    date_birth = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата рождения"
    )

    def save(self, *args, **kwargs):
        super().save()

        photo = Image.open(self.photo.path)

        if photo.height > 250 or photo.width > 250:
            new_photo = (250, 250)
            photo.thumbnail(new_photo)
            photo.save(self.photo.path)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
