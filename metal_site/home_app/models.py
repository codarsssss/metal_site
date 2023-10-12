from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Наименование категории"
    )  # наименование категории
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField(
        blank=True, verbose_name="Описание категории"
    )  # описание категории
    image = models.ImageField(upload_to="products/")  # установить pillow!

    class Meta:
        ordering = ("slug",)
        verbose_name = "Категория продукции"
        verbose_name_plural = "Категории продукции"

    def __str__(self) -> str:
        return f"{self.title}"


class Product(models.Model):
    class UnitOfMeasure(models.TextChoices):
        EA = "EA", "шт."
        LINEAR_METER = "LIN_M", "пог. м."
        SQUARE_METER = "SQ_M", "кв. м."
        TON = "T", "т."

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
        ordering = ("title",)
        verbose_name = "Продукция"

    def __str__(self) -> str:
        return f"{self.designation} - {self.title}"
