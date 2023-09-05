# importing contactSerializer, smsSerializer, voiceMailSerializer, userSerializer from serializers.py
from .serializers import ContactSerializer, SmsSerializer, VoiceMailSerializer
# importing Contact, Sms, VoiceMail, User from models.py
from .models import Contact, Sms, VoiceMail, User

# importing rest_framework's
from rest_framework import viewsets, permissions, generics


# create generics view for creating a contact
class CreateContactView(generics.CreateAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
#    permission_classes = [permissions.IsAuthenticated]
    
    # overriding the perform_create method
    def perform_create(self, serializer):
        # setting the user field of the serializer to the current user
        serializer.save(user=self.request.user)
        
# creating list view for listing all the contacts of the current user
class ContactListView(generics.ListAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
#    permission_classes = [permissions.IsAuthenticated]
    
    # overriding the get_queryset method
    def get_queryset(self):
        # returning the contacts of the current user
        return Contact.objects.filter(user=self.request.user)
    
# view to delete a contact
class DeleteContactView(generics.DestroyAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
    permission_classes = [permissions.IsAuthenticated]
    
# view to update a contact
class UpdateContactView(generics.UpdateAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
    permission_classes = [permissions.IsAuthenticated]
    
    # overriding the get_queryset method
    def get_queryset(self):
        # returning the contacts of the current user
        return Contact.objects.filter(user=self.request.user)
    
# view for searching contacts
class SearchContactView(generics.ListAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
    permission_classes = [permissions.IsAuthenticated]
# overriding the get_queryset method and use query search param to search for contacts
    def get_queryset(self):
        # getting the query search param
        query = self.request.query_params.get('search')
        # returning the contacts of the current user
        return Contact.objects.filter(user=self.request.user, contact_name__icontains=query)
    
# view for retrieving a contact
class Contact(generics.RetrieveAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.all()