# Generated by Django 5.2 on 2025-04-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mojodi',
            field=models.BooleanField(default=True),
        ),
    ]
