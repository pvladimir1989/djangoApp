from django.contrib import admin
from django.contrib.admin import ModelAdmin

from testapp.models import Book, UserBookRelation


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass


@admin.register(UserBookRelation)
class BookAdmin(ModelAdmin):
    pass
