from django.contrib.auth.models import User, Permission
from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from .models import Product, Order, Market


class ProductsListViewTestCase(TestCase):

    def test_orders_view(self):
        response = self.client.get(reverse('app_market:products-map'))
        self.assertContains(response, 'Products')


class ProductDetailsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name='Best Product')

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse('app_market:product', kwargs={'pk': self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse('app_market:product', kwargs={'pk': self.product.pk})
        )
        self.assertContains(response, self.product.name)


class SalesStatisticViewTestCase(TestCase):
    def test_statistic(self):
        response = self.client.get('/marketplace/stat/')

        self.assertEqual(response.status_code, 200)
