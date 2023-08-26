from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='homepage'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/edit/', BlogUpdateView.as_view(), name='edit_blog'),
    path('blog/delete/', BlogDeleteView.as_view(), name='delete_blog')
]
