from django.shortcuts import render



def index(request):
    return render(request, 'stepshop/index.html')


def contacts(reqest):
    return render(reqest, 'stepshop/contact.html')


def about(reqest):
    return render(reqest, 'stepshop/about.html')
