# Generated by Django 4.2.6 on 2025-01-26 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_product_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deportament',
        ),
    ]
