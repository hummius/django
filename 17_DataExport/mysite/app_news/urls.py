from django.urls import path
from app_news.views import get_news_in_custum_format, NewsItemDetailView

urlpatterns = [
    path('', get_news_in_custum_format, name='news-list'),
    path('<int:pk>', NewsItemDetailView.as_view(), name='news-item')
]
