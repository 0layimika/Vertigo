# Generated by Django 4.2.4 on 2023-09-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]