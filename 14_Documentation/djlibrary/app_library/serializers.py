from rest_framework import serializers
from app_library.models import Book, Autor


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'release', 'pages', 'autor']


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['name', 'last_name', 'birth']
