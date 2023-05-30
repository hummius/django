from django.urls import path
from app_pages.views import welcome, main_page
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('welcome/', cache_page(30)(welcome), name='welcome'),
    path('main_page/', main_page, name='main-page'),
]