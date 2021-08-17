from django.urls import path
from .views import products


app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]
