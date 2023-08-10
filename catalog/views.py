from django.shortcuts import render


def homepage(request):
    return render(request, 'catalog/homepage.html')


def contact_information(request):
    return render(request, 'catalog/contact_information')
