from django.shortcuts import render
from mainapp.models import Product


def products(req):
    links_manu = [
        {'data_filter': '*', 'name': 'All Products'},
        {'data_filter': '.new', 'name': 'Newest'},
        {'data_filter': '.low', 'name': 'Low Price'},
        {'data_filter': '.high', 'name': 'Hight Price'},
    ]

    products_data = Product.objects.all()

    context = {
        'links_menu': links_manu,
        'products': products_data
    }

    return render(request=req,template_name='mainapp\products.html', context=context)
