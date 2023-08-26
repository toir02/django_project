from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/homepage.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description')
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'catalog/blog_list.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('catalog:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')