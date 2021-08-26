from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


def products(req, pk=None):

    links_menu = ProductCategory.objects.all()
    products_data = Product.objects.all().order_by('price')
    context = {
        'links_menu': links_menu,
        'products': products_data
    }

    if pk is not None:
        if pk == 0:
            products_data = Product.objects.all().order_by('price')
            category = {'name': 'all', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_data = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'links_menu': links_menu,
            'products': products_data
        }

    return render(request=req,template_name='mainapp/products.html', context=context)
