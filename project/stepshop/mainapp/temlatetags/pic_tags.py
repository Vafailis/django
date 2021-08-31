from django import template
from django.conf import settings


register = template.Library()


@register.filter(name='media_folder_products')
def media_folder_products(string):
    if not string:
        string = 'product_images/default.png'
    return f'{settings.MEDIA_URL}{string}'
