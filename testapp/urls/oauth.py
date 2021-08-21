from django.urls import path, include

from testapp.views import auth

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)

]