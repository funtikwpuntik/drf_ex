# Generated by Django 4.2.2 on 2024-11-04 09:25
# pylint: disable=all
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('drf', '0004_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
