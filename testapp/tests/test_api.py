from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from testapp.models import Book
from testapp.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book1 = Book.objects.create(name='test1', price=5, author_name='test1')
        self.book2 = Book.objects.create(name='test2', price=5, author_name='test5')
        self.book3 = Book.objects.create(name='test3', price=5, author_name='test1')

    def test_get(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(response.data)

    def test_get_search(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url, data={'search': 'test1'})
        serializer_data = BooksSerializer([self.book1, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(response.data)
