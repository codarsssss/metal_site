from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Наименование категории"
    )  # наименование категории
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField(
        blank=True, verbose_name="Описание категории"
    )  # описание категории
    image = models.ImageField(upload_to="media/", default="no_image.png")

    class Meta:
        ordering = ("slug",)
        verbose_name = "Категория продукции"
        verbose_name_plural = "Категории продукции"

    def get_absolute_url(self):
        return reverse("home_app:category_detail", args=[self.slug])

    def __str__(self) -> str:
        return f"{self.title}"


class Product(models.Model):
    class UnitOfMeasure(models.TextChoices):
        EA = "шт.", "шт."
        LINEAR_METER = "пог. м.", "пог. м."
        SQUARE_METER = "кв. м.", "кв. м."
        TON = "т.", "т."

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=64, verbose_name="Наименование")
    designation = models.CharField(max_length=64, verbose_name="Обозначение")
    material = models.CharField(max_length=64, verbose_name="Материал")
    units_of_measure = models.CharField(
        max_length=8,
        choices=UnitOfMeasure.choices,
        default=UnitOfMeasure.TON,
        verbose_name="Единица измерения",
    )
    price_for_unit = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Цена за единицу"
    )
    in_stock = models.DecimalField(
        max_digits=10, decimal_places=3, verbose_name="На складе"
    )
    is_in_stock = models.BooleanField(default=True, verbose_name="Наличие")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        ordering = ("designation",)
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

    def __str__(self) -> str:
        return f"{self.designation} - {self.title}"


class Feedback(models.Model):
    name = models.CharField(max_length=64, verbose_name="Имя")
    email = models.EmailField(max_length=128, verbose_name="Электронный адрес (email)")
    contact_number = models.CharField(
        unique=True, verbose_name="Контактный номер", max_length=12
    )
    comment = models.TextField(verbose_name="Содержание послания")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ["-time_create"]

    def __str__(self):
        return f"{self.contact_number}-{self.name}:{self.time_create}"


class FilePrice(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price_file = models.FileField(
        upload_to="home_app/%Y",
        verbose_name="Актуальный прайс",
        null=True,
        default="test_price.pdf",
    )

    class Meta:
        verbose_name = "Prices"
        verbose_name_plural = "Price"
        ordering = ["-time_create"]
