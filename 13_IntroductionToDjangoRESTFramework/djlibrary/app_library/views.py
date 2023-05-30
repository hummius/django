from rest_framework.mixins import ListModelMixin
from app_library.models import Book, Autor
from app_library.serializers import BookSerializer, AutorSerializer
from rest_framework.generics import GenericAPIView
from app_library.pagination import ResultPagePagination


class BookList(GenericAPIView, ListModelMixin):
    serializer_class = BookSerializer
    pagination_class = ResultPagePagination

    def get_queryset(self):
        queryset = Book.objects.all()
        book_name = self.request.query_params.get('name')
        book_autor = self.request.query_params.get('autor')
        book_pages = self.request.query_params.get('pages')
        less_pages = self.request.query_params.get('less_pages')
        more_pages = self.request.query_params.get('more_pages')

        if book_name:
            queryset = queryset.filter(name=book_name)
        if book_autor:
            queryset = queryset.filter(autor=book_autor)
        if book_pages:
            queryset = queryset.filter(pages=book_pages)
        if less_pages:
            queryset = queryset.filter(pages__lt=less_pages)
        if more_pages:
            queryset = queryset.filter(pages__gt=more_pages)

        return queryset

    def get(self, request):
        return self.list(request)


class AutorList(GenericAPIView, ListModelMixin):
    serializer_class = AutorSerializer
    pagination_class = ResultPagePagination

    def get_queryset(self):
        queryset = Autor.objects.all()
        autor_name = self.request.query_params.get('name')
        if autor_name:
            queryset = queryset.filter(name=autor_name)
        return queryset

    def get(self, request):
        return self.list(request)
