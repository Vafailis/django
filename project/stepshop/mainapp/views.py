from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from stepshop.views import get_basket_quentity

def products(req, pk=None):
    context = {
        'links_menu': ProductCategory.objects.all(),
        'products': Product.objects.all().order_by('price')
    }

    basket = []

    if req.user.is_authenticated:
        basket = Basket.objects.filter(user=req.user)


    if pk is not None:
        context['products'] = Product.objects.filter(category__pk=pk).order_by('price')
    context['basket'] = basket

    return render(request=req,template_name='mainapp/products.html', context=context)


def product(request, pk):
    context = {
        'links_menu': ProductCategory.objects.all(),
        'all_products': Product.objects.filter(category__pk=ProductCategory.objects.get(name=Product.objects.get(pk=pk).category).pk).exclude(pk=pk),
        'product': get_object_or_404(Product, pk=pk),
        'basket':get_basket_quentity(request),
        'category_id': ProductCategory.objects.get(name=Product.objects.get(pk=pk).category).pk
    }

    return render(request=request,template_name='mainapp/product.html', context=context)
