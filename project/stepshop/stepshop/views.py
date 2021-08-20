from django.shortcuts import render
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]

    context = {
        'products': products,
    }

    return render(request, 'stepshop/index.html', context=context)


def contacts(reqest):
    return render(reqest, 'stepshop/contact.html')


def about(reqest):
    return render(reqest, 'stepshop/about.html')
