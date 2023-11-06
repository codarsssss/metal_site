from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(
        upload_to="users/%Y", blank=True, null=True, verbose_name="Фотография"
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
