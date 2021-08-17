from django.shortcuts import render


def products(req):
    return render(req, 'mainapp\products.html')
