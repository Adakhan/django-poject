# Generated by Django 2.2.1 on 2019-05-24 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_product_owner_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_owner_info',
        ),
    ]
