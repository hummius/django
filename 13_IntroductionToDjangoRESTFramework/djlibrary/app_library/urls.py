from django.urls import path
from app_library.views import BookList, AutorList

urlpatterns = [
    path('books/', BookList.as_view(), name='books_list'),
    path('autors/', AutorList.as_view(), name='autors_list'),
]