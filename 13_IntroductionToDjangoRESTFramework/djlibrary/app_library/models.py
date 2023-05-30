from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=50, unique=True, primary_key=True, verbose_name='фамилия')
    birth = models.IntegerField(verbose_name='год рождения')


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    isbn = models.CharField(max_length=100)
    release = models.IntegerField(verbose_name='год выпуска')
    pages = models.IntegerField(verbose_name='количество страниц')
    autor = models.ForeignKey(Autor, to_field='last_name', null=True, on_delete=models.CASCADE, verbose_name='автор')
