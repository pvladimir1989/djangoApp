from django.urls import path, include
from rest_framework import routers

from testapp.views import index, BooksViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
# router.register(r'auto', AutoListView)
# router.register(r'services', ServicesListView)
# router.register(r'someitems', SomeItemsListView)

urlpatterns = [
    # path('v1/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    router.urls
]