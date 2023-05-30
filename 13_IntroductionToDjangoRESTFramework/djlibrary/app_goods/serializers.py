from rest_framework import serializers
from app_goods.models import Item, ItemsGroup


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'weight', 'group']


class ItemsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsGroup
        fields = ['id', 'name']
