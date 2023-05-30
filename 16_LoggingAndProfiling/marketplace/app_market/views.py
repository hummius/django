from django.shortcuts import render, redirect, get_object_or_404
from app_market.models import *
from app_market.utils import make_all_changes
from app_users.models import UserProfile
from django.db import transaction
from django.http import HttpRequest, HttpResponse

from app_users.utils import reduce_balance
import logging


logger = logging.getLogger(__name__)


def products_list_market(request, *args, **kwargs):
    products = Product.objects.all()
    items = ItemPosition.objects.select_related('market').prefetch_related('product').all()

    context = {
        'products': products,
        'objects_list': items
    }

    return render(request, 'app_market/products-map.html', context=context)


def product_details(request, pk):

    product = Product.objects.get(id=pk)
    items = ItemPosition.objects.filter(product_id=pk)

    context = {
        'product': product,
        'positions': items
    }

    return render(request, 'app_market/product.html', context=context)


def add_to_cart(request):

    cart = Cart(request)
    product = get_object_or_404(Product, id=int(request.POST['product_id']))
    cart.add(product, quantity=int(request.POST['amount']),
             update_quantity=int(request.POST['amount']),
             market_id=int(request.POST['market_id']),
             position_id=int(request.POST['item_id']))
    return products_list_market(request)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('app_market:cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'app_market/cart.html', {'cart': cart, 'full_price': cart.__len__()})


def make_order(request):
    profile = UserProfile.objects.get(user_id=request.user.id)
    if profile.balance >= int(request.POST['full_price']):
        with transaction.atomic():
            reduce_balance(user_profile=profile, check=int(request.POST['full_price']))
            make_all_changes(cart=Cart(request), user_id=request.user.id)
        logger.info('Оформление заказа.')
        return redirect('app_market:cart')

    else:
        logger.info('Оформление заказа(НЕУДАЧА: не средств на балансе')
        return HttpResponse('Не достаточно средств на балансе')


def sales_statistic(request):
    products = Product.objects.order_by('-sales')
    return render(request, 'app_market/sales-statistic.html', {'products': products})

