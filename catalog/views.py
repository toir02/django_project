from django.shortcuts import render

from catalog.models import Product


def homepage(request):
    context = {
        'object_list': Product.objects.all().order_by('id')
    }
    return render(request, 'catalog/homepage.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context=context)
