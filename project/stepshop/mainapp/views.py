from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


def products(req, pk=None):
    context = {
        'links_menu': ProductCategory.objects.all(),
        'products': Product.objects.all().order_by('price')
    }

    if pk is not None:
        context['products'] = Product.objects.filter(category__pk=pk).order_by('price')

    return render(request=req,template_name='mainapp/products.html', context=context)


def product(request, pk):
    context = {
        'links_menu': ProductCategory.objects.all(),
        'all_products': Product.objects.filter(category__pk=ProductCategory.objects.get(name=Product.objects.get(pk=pk).category).pk).exclude(pk=pk),
        'product': get_object_or_404(Product, pk=pk)
    }

    return render(request=request,template_name='mainapp/product.html', context=context)
