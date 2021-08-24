from django.urls import path
from .views import products
from django.conf import settings
from django.conf.urls.static import static


app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

