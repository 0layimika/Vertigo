# Generated by Django 4.2.4 on 2023-09-01 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
