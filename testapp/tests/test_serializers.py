from django.test import TestCase

from testapp.models import Book
from testapp.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price=25, author_name='Author 1')
        book_2 = Book.objects.create(name='Test book 2', price=55, author_name='Author 2')
        serializer_data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [{
            'id': book_1.id,
            'name': 'Test book 1',
            'price': '25.00',
            'author_name': 'Author 1'
        },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
                'author_name': 'Author 2'
            },
        ]

        self.assertEqual(serializer_data, expected_data)
