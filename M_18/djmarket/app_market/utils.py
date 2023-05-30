from django.contrib.auth.models import User

from app_market.models import Product, Order, ItemPosition


def make_all_changes(cart, user_id):
    product_ids = cart.cart.keys()
    prod = Product.objects.filter(id__in=product_ids)

    for item in cart.cart.values():
        position = ItemPosition.objects.get(id=int(item['position_id']))
        position.amount -= int(item['quantity'])
        position.save()

    user = User.objects.get(id=user_id)

    order = Order.objects.create(
        user=user,
        order_price=cart.__len__(),
    )
    order.products.set(prod)

    for product in prod:
        product.sales += cart.cart[str(product.id)]['quantity']
        product.save()

    cart.clear()