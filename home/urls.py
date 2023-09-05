from .api_views import get_contacts, add_contact
from django.urls import path

urlpatterns = [
    path('get_contacts/', get_contacts, name='get_contacts'),
    path('add_contact/', add_contact, name='add_contact'),
]