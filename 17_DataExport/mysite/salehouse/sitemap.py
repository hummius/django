from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from salehouse.models import SaleHouseNews


class StaticSitemap(Sitemap):
    def items(self):
        return ['about-us', 'contacts']

    def location(self, item):
        return reverse(item)


class SaleHouseNewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority =0.9

    def items(self):
        return SaleHouseNews.objects.filter(is_published=True).all()

    def lastmod(self, obj: SaleHouseNews):
        return obj.published_at