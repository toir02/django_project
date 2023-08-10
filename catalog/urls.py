from django.urls import path

from catalog.views import homepage, contact_information

urlpatterns = [
    path('homepage', homepage),
    path('contact_information', contact_information)
]
