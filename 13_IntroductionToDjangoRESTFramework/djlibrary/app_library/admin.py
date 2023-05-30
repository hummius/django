from django.contrib import admin
from app_library.models import Book, Autor


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'autor', 'isbn', 'release', 'pages']


admin.site.register(Book, BookAdmin)


class AutorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'name', 'birth']


admin.site.register(Autor, AutorAdmin)
