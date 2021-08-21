from django.urls import path
from rest_framework.routers import SimpleRouter

from testapp.views import index, BooksViewSet
from django.contrib import admin

router = SimpleRouter()

router.register(r'book', BooksViewSet)

urlpatterns = [

    path('', index, name='index'),
    path('admin/', admin.site.urls),

]

urlpatterns += router.urls
