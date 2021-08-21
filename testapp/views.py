from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from testapp.models import Book
from testapp.serializers import BooksSerializer


def index(request: HttpRequest) -> HttpResponse:
    turn_on_block = settings.MAINTENANCE_MODE

    return render(request, 'main/index.html', {
        "turn_on_block": turn_on_block,
    })


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']


def auth(request):
    return render(request, 'main/oauth.html')
