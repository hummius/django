# Generated by Django 4.0.6 on 2023-05-09 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0003_product_sales_alter_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=200, verbose_name='offer')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(max_length=200, verbose_name='promotion')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_market.product', verbose_name='product')),
            ],
        ),
    ]
