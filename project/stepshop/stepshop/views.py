from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def contacts(reqest):
    return render(reqest, 'contact.html')


def about(reqest):
    return render(reqest, 'about.html')
