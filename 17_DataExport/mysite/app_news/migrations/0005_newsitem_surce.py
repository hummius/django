# Generated by Django 4.0.6 on 2023-05-08 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0004_newssource'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='surce',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='app_news.newssource'),
        ),
    ]
