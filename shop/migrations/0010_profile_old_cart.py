# Generated by Django 5.2 on 2025-05-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
