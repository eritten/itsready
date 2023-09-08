from .api_views import get_contacts, add_contact, search_contact, delete_contact, update_contact
from django.urls import path
# importing format suffix patterns
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('get_contacts/', get_contacts, name='get_contacts'),
    path('add_contact/', add_contact, name='add_contact'),

    path('search_contact/', search_contact, name='search_contact'),
    path('delete_contact/', delete_contact, name='delete_contact'),
    path('update_contact/', update_contact, name='update_contact'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

