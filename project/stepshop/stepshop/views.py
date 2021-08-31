from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket


def get_basket_quentity(request):
    if request.user.is_authenticated:
        return Basket.objects.filter(user=request.user)


def index(request):
    products = Product.objects.all()


    context = {
        'products': products,
        'basket': get_basket_quentity(request),
    }

    return render(request, 'stepshop/index.html', context=context)


def contacts(request):
    return render(request, 'stepshop/contact.html', context={'basket': get_basket_quentity(request),})


def about(request):
    return render(request, 'stepshop/about.html', context={'basket': get_basket_quentity(request),})
