from django.shortcuts import render


def products(req):
    title = 'продукты | каталог'

    links_manu = [
        {'data_filter': '*', 'name': 'All Products'},
        {'data_filter': '.new', 'name': 'Newest'},
        {'data_filter': '.low', 'name': 'Low Price'},
        {'data_filter': '.high', 'name': 'Hight Price'},
    ]

    context = {
        'title':title,
        'links_menu': links_manu,
    }

    return render(request=req,template_name='mainapp\products.html', context=context)
