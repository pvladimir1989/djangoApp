import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from testapp.models import Book
from testapp.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
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

    def test_create(self):
        self.assertEqual(3, Book.objects.all().count())
        url = reverse('book-list')
        data = {
            "name": "Programming",
            "price": 150,
            "author_name": "Mark S"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Book.objects.all().count())

    def test_update(self):
        url = reverse('book-detail', args=(self.book1.id,))
        data = {
            "name": self.book1.name,
            "price": 575,
            "author_name": self.book1.author_name
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.book1 = Book.objects.get(id=self.book1.id)
        self.book1.refresh_from_db()
        self.assertEqual(575, self.book1.price)

        # self.assertEqual(4, Book.objects.all().count())

    def test_delete(self):
        url = reverse('book-detail', args=(self.book1.id,))
        # data = {
        #     "name": self.book1.name,
        #     "price": 575,
        #     "author_name": self.book1.author_name
        # }
        # json_data = json.dumps(data)
        # self.client.force_login(self.user)
        # response = self.client.put(url, data=json_data, content_type='application/json')
        response=self.client.delete(url,data=None,content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.book1 = Book.objects.get(id=self.book1.id)
        self.book1.refresh_from_db()
        self.assertEqual(575, self.book1.price)

        # self.assertEqual(4, Book.objects.all().count())
