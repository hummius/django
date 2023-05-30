from _decimal import Decimal

from django.db import models
from app_users.models import User
from marketplace import settings


class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]
        verbose_name_plural = 'товар'
        verbose_name = 'товар'

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(null=False, blank=True, verbose_name='описание')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    sales = models.PositiveIntegerField(default=0, verbose_name='продажи')

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='покупатель')
    products = models.ManyToManyField(Product, related_name="orders", verbose_name='наименования')
    order_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='сумма заказа')

    class Meta:
        verbose_name_plural = 'заказы'
        verbose_name = 'заказ'


class Market(models.Model):
    class Meta:
        verbose_name_plural = 'магазины'
        verbose_name = 'магазин'

    name = models.CharField(max_length=30, verbose_name='название магазина')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='создано')


    def __str__(self):
        return f"Магазин(pk={self.pk}, name={self.name!r})"


class ItemPosition(models.Model):
    class Meta:
        verbose_name_plural = 'позиции товаров'
        verbose_name = 'позиция товара'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='наименование товара')
    amount = models.PositiveIntegerField(verbose_name='кол-во')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=True, verbose_name='в магазине')


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, market_id, position_id, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'position_id': position_id,
                                     'market_id': market_id}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """Удаление товара из карзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор элементов в карзине и получение продуктов из базы данных"""
        full_price = [0]
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['quantity'])
            full_price[0] += item['total_price']
            yield item


    def __len__(self):
        """Подсчет всей суммы в корзине"""
        full_price = [0]
        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])
            full_price[0] += int(item['total_price'])
        return full_price[0]

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

