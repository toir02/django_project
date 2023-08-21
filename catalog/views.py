from django.shortcuts import render

from catalog.models import Product


def homepage(request):
    return render(request, 'catalog/homepage.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/products.html', context=context)
