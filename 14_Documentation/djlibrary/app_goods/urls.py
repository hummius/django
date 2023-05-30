from django.urls import path
from app_goods.views import ItemList, ItemGroupList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='items_list'),
    path('item-groups/', ItemGroupList.as_view(), name='item_groups_list'),
    path('item-detail/<int:pk>/', ItemDetail.as_view(), name='item_details'),
]
