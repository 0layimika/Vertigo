# Generated by Django 4.2.4 on 2023-09-01 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]