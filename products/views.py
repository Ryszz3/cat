from pprint import pprint

from django.db import connection
from django.shortcuts import render

from products.models import Book


def index(request):
    data = Book.objects.all().select_related("author")
    r = render(request, 'index.html', context={"data":data})
    pprint(connection.queries)
    return r
