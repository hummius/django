from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render
from django.core import serializers
from django.views import generic

from salehouse.models import SaleHouse, SaleHouseNews


def get_news_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, SaleHouseNews.objects.all())
    return HttpResponse(data)


class HousesListView(generic.ListView):
    context_object_name = "houses"
    queryset = SaleHouse.objects.filter(sold=False)
    template_name = 'salehouse/houses-list.html'


def about_us(request):
    return render(request, 'salehouse/about-us.html')


def contacts(request):
    return render(request, 'salehouse/contacts.html')


class NewsDetailView(generic.DetailView):
    model = SaleHouseNews
    template_name = 'salehouse/news.html'

