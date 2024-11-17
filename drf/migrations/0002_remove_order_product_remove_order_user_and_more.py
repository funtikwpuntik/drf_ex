# Generated by Django 5.1.2 on 2024-10-31 09:12
# pylint: disable=all
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('drf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='warehouse',
        ),
        migrations.DeleteModel(
            name='ApiUser',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
    ]
