from django.urls import path
from salehouse.views import HousesListView, about_us, contacts, get_news_in_custom_format, NewsDetailView

urlpatterns = [
    path('', HousesListView.as_view(), name='sale-list'),
    path('about-us/', about_us, name='about-us'),
    path('contacts/', contacts, name='contacts'),
    path('news/', get_news_in_custom_format, name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='sale-news'),
]