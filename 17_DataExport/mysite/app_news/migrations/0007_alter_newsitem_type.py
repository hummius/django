# Generated by Django 4.0.6 on 2023-05-08 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_newsitem_description_alter_newsitem_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='app_news.newstype'),
        ),
    ]
