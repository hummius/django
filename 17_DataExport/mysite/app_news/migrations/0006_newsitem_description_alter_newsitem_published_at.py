# Generated by Django 4.0.6 on 2023-05-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_newsitem_surce'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='description',
            field=models.TextField(default='', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='дата публикации'),
        ),
    ]