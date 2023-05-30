from django.urls import path
from app_market.views import *


app_name = 'app_market'

urlpatterns = [
    path('products/', products_list_market, name='products-map'),
    path('product/<int:pk>/', product_details, name='product'),
    path('to-cart/', add_to_cart, name='to-cart'),
    path('cart/', cart_detail, name='cart'),
    path('cart_remove/<product_id>/', cart_remove, name='cart-remove'),
    path('make-order/', make_order, name='make-order'),
    path('stat/', sales_statistic, name='sales-statistic'),
]