from django.shortcuts import render

from catalog.models import Product


def homepage(request):
    return render(request, 'catalog/homepage.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context=context)
