from .urls import urlpatterns as base_urlpatterns
from .oauth import urlpatterns as oauth_urlpatterns

urlpatterns = []
urlpatterns += base_urlpatterns
urlpatterns += oauth_urlpatterns
