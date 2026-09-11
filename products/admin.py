from django.contrib import admin

from products.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["author"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["name"]
