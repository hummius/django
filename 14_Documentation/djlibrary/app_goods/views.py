from rest_framework import status
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from app_goods.models import Item, ItemsGroup
from app_goods.serializers import ItemSerializer, ItemsGroupSerializer
from rest_framework.generics import GenericAPIView


class ItemList(GenericAPIView, ListModelMixin, CreateModelMixin):
    #queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ItemGroupList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = ItemsGroup.objects.all()
    serializer_class = ItemsGroupSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ItemDetail(GenericAPIView, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
