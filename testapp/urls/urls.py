import debug_toolbar
from django.conf import settings
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from testapp.views import index, BooksViewSet, UserBooksRelationView
from django.contrib import admin

router = SimpleRouter()

router.register(r'book', BooksViewSet)
router.register(r'book_relation', UserBooksRelationView)

urlpatterns = [

    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    # path('__debug__/', include(debug_toolbar.urls)),

]

urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
