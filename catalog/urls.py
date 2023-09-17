from django.urls import path
from django.views.decorators.cache import never_cache

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('product/edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='edit_product'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('blog/create/', never_cache(BlogCreateView.as_view()), name='create_blog'),
    path('blog/edit/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='edit_blog'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog')
]
