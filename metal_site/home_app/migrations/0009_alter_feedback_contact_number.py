# Generated by Django 4.2.6 on 2023-10-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_alter_product_units_of_measure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='contact_number',
            field=models.CharField(max_length=12, unique=True, verbose_name='Контактный номер'),
        ),
    ]
