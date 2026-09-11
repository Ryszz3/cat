from django.db import models
from django.forms import CharField


# Создай небольшое Django-приложение с моделями Author и Book:
# у каждой книги один автор (ForeignKey). Добавь несколько авторов и книг через админку.
# Сделай страницу со списком книг, где выводятся название книги и имя автора.
# Сначала реализуй обычный запрос, затем перепиши его с select_related

class Author(models.Model):
    name = models.CharField(max_length=100, default="a")

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)