from .api_views import get_contacts, add_contact, search_contact, delete_contact, update_contact, change_password, change_email, change_username, create_account, delete_account, MyTokenObtainPairView, add_note, get_notes, delete_note, update_note
from django.urls import path
# importing format suffix patterns
from rest_framework.urlpatterns import format_suffix_patterns
from .validate import generate, reset, validate_code

urlpatterns = [
    path('get_contacts/', get_contacts, name='get_contacts'),
    path('add_contact/', add_contact, name='add_contact'),

    path('search_contact/', search_contact, name='search_contact'),
    path('delete_contact/', delete_contact, name='delete_contact'),
    path('update_contact/', update_contact, name='update_contact'),
    path('change_password/', change_password, name='change_password'),
    path('change_email/', change_email, name='change_email'),
    path('change_username/', change_username, name='change_username'),
    path('create_account/', create_account, name='create_account'),
    path('delete_account/', delete_account, name='delete_account'),
    path('generate/', generate, name='generate'),
    path('reset/', reset, name='reset'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('validate/', validate, name='validate'),
    path('validate/', validate_code, name='validate_code'),
    path('add_note/', add_note, name='add_note'),
    path('get_notes/', get_notes, name='get_notes'),
    path('delete_note/', delete_note, name='delete_note'),
    path('update_note/', update_note, name='update_note'),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

