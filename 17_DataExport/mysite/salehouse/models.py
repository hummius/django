from django.db import models
from django.urls import reverse


class SaleHouse(models.Model):
    address = models.CharField(max_length=120, verbose_name='адрес')
    sold = models.BooleanField(default=False, verbose_name='продано')
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, related_name='house', null=True)
    number_rooms = models.ForeignKey('NumberOfRooms', on_delete=models.CASCADE, related_name='house', null=True)

    class Meta:
        verbose_name = 'жилье'
        verbose_name_plural = 'жилье'


class RoomType(models.Model):
    type = models.CharField(max_length=120, verbose_name='тип помещения')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'тип помещения'
        verbose_name_plural = 'типы помещений'

    def __str__(self):
        return self.type


class NumberOfRooms(models.Model):
    number = models.PositiveIntegerField(default=1, verbose_name='кол-во комнат')

    def __str__(self):
        return str(self.number)


class SaleHouseNews(models.Model):
    title = models.CharField(max_length=120, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст записи')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='создано')
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(verbose_name='дата публикации', null=True)
    description = models.TextField(verbose_name='описание', default='')

    def get_absolute_url(self):
        return reverse('news-item', args=[str(self.id)])

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title
