from django.shortcuts import render

from catalog.models import Product


def homepage(request):
    context = {
        'object_list': Product.objects.all().order_by('id')
    }
    return render(request, 'catalog/homepage.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'product': product_item,
    }
    return render(request, 'catalog/product.html', context=context)
