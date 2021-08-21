from django.urls import include,path
from rest_framework.routers import SimpleRouter

from testapp.views import index, BooksViewSet
from django.contrib import admin

router = SimpleRouter()

router.register(r'book', BooksViewSet)

urlpatterns = [

    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),

]

urlpatterns += router.urls
