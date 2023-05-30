from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from salehouse.models import SaleHouseNews


class LatestNewsFeed(Feed):
    title = 'Новости'
    link = '/sitenews/'
    description = 'Самые свежие новости.'

    def items(self) -> QuerySet:
        return SaleHouseNews.objects.order_by('published_at')[:10]

    def item_title(self, item: SaleHouseNews) -> str:
        return item.title

    def item_description(self, item: SaleHouseNews) -> str:
        return item.description

    def item_link(self, item: SaleHouseNews) -> str:
        return reverse('sale-news', args=[item.pk])
