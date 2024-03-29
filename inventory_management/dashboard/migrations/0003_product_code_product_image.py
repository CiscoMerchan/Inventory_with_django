# Generated by Django 4.1.7 on 2023-04-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_client_supplier_purchaseorder_clientorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/static/img/product.png', upload_to='product_images'),
        ),
    ]
