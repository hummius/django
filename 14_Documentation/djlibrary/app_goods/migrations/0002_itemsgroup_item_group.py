# Generated by Django 4.0.6 on 2023-05-02 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='group', max_length=200, verbose_name='название')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_goods.itemsgroup', verbose_name='группа'),
        ),
    ]
