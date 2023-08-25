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
    permission_classes = [permissions.IsAuthenticated]
    
    # overriding the perform_create method
    def perform_create(self, serializer):
        # setting the user field of the serializer to the current user
        serializer.save(user=self.request.user)
        
# creating list view for listing all the contacts of the current user
class ContactListView(generics.ListAPIView):
    # setting the serializer class
    serializer_class = ContactSerializer
    # setting the permission class
    permission_classes = [permissions.IsAuthenticated]
    
    # overriding the get_queryset method
    def get_queryset(self):
        # returning the contacts of the current user
        return Contact.objects.filter(user=self.request.user)