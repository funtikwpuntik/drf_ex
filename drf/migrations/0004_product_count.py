# Generated by Django 4.2.2 on 2024-11-01 07:23
# pylint: disable=all
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('drf', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
