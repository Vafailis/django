from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def contacts(reqest):
    return render(reqest, 'contact.html')


def products(reqest):
    return render(reqest, 'products.html')


def about(reqest):
    return render(reqest, 'about.html')


def single(reqest):
    return render(reqest, 'single-product.html')
