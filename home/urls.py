from .api_views import CreateContactView, ContactListView
from django.urls import path

urlpatterns = [
    # path for creating a contact
    path('create-contact/', CreateContactView.as_view(), name='create_contact'),
    # path for listing all contacts
    path('list-contacts/', ContactListView.as_view(), name='list_contacts'),
]
