from pprint import pprint

from django.db import connection
from django.db.models import Q, Count
from django.shortcuts import render

from products.models import Book, Author, Category


def index(request):
    """
    отображает главную страницу, не создает N+1 запросов к базе

    :param request:
    :return:{'data': <QuerySet [<Book>]>, 'categories': <QuerySet [<Category>]>}
    """
    data = Book.objects.all().select_related("author").prefetch_related("category")
    cats = Category.objects.annotate(books_count=Count('books'))
    context = {
        "data": data,
        "categories": cats,
    }
    print(context)
    r = render(request, 'index.html', context=context)
    pprint(connection.queries)
    return r

def search(request):
    """
    ищет в базе данные по полученным квери параметрам
    :param request: <QueryDict: {'search': [str], 'category': [str]}>
    :return:
    """
    if request.method == "GET":
        print(request.GET)
        search_field = request.GET.get('search')
        categories = request.GET.getlist('category')
        sort_by_name = request.GET.get("sort_by_name")
        sort_by_price = request.GET.get("sort_by_price")
        ordering = [] # формирование строки сортировки по убыванию/возрастанию цены/имени
        if sort_by_price == "high":
            ordering.append("-price")
        else:
            ordering.append("price")
        if sort_by_name == "za": # "za" значит сортировку от "z" до "A" то есть против алфавита
            ordering.append("-name")
        else:
            ordering.append("name")
        # формирование запроса к базе в зависимости от введенных символов в строку поиска,
        # поиск работает по совпадению символов в имени книги/имени категории
        # в конце задается порядок отображения в зависимости какую фильтрацию выбрал пользователь
        data = Book.objects.filter(Q(Q(name__icontains=search_field) | Q(category__name__icontains=search_field))).distinct().order_by(*ordering)
        print(data)
        # если выбрана галочка/галочки сортировки по категориям, здесь отметаются ненужные записи
        if categories:
            data = data.filter(category__name__in=categories)

        context = {
            "data": data,

        }
        return render(request, 'index.html', context=context)
