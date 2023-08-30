from .api_views import CreateContactView, ContactListView, UpdateContactView, DeleteContactView
from django.urls import path

urlpatterns = [
    # path for creating a contact
    path('create-contact/', CreateContactView.as_view(), name='create_contact'),
    # path for listing all contacts
    path('list-contacts/', ContactListView.as_view(), name='list_contacts'),

    # path for updating a contact
    path('update-contact/<int:pk>/', UpdateContactView.as_view(), name='update_contact'),

    # path for deleting a contact
    path('delete-contact/<int:pk>/', DeleteContactView.as_view(), name='delete_contact'),
    
]
