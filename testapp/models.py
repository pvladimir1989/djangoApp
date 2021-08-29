from django.contrib.auth.models import User
from django.db import models

RATE_CHOICES = (
    (1, 'Ok'),
    (2, 'Fine'),
    (3, 'Good'),
    (4, 'Amazing'),
    (5, 'Incredible')
)


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books')
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    def __str__(self):
        # в админке отображается id и name
        return f'Id {self.id}:{self.name}'


class UserBookRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES,null=True)

    def __str__(self):
        # в админке отображается id и name
        return f'Id {self.user.username}:{self.book.name}, RATE {self.rate}'
