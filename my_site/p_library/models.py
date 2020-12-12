from django.db import models
from django.contrib import admin


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    verbose_name = "Автор"  # name in admin panel
    verbose_name_plural = "Aвторы"

    def __str__(self):
        return f'{self.full_name} \n'


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=19, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # models.CASCADE say that if Author was delete all
    # book with id author was delete too
    verbose_name = "Книга"  # name in admin panel
    verbose_name_plural = "Книги"

    def __str__(self):
        return f'{self.title} \n'


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    verbose_name = "Издательство"
    verbose_name_plural = "Издательства"

    def __str__(self):
        return f'{self.name} \n'
