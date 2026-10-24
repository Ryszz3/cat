from django.contrib import admin
from django.db.models import Sum

from products.models import Book, Author, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["author", "category", "name", "price"]
    list_display = ["pk", "name", "author", "price"]
    search_fields = ["name__icontains"]
    ordering = ["name", "price"]
    list_editable = ["name", "price", "author"]

    # @admin.display(description="Summary order price")
    # def summ(self):
    #     summary = Book.objects.values("price").aggregate(Sum("price"))
    #     return summary.get('price__sum')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["pk", "name"]
    list_editable = ["name"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["pk", "name"]
    list_editable = ["name"]
