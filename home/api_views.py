# importing contactSerializer, smsSerializer, voiceMailSerializer, userSerializer from serializers.py
from .serializers import ContactSerializer, SmsSerializer, VoiceMailSerializer
# importing Contact, Sms, VoiceMail, User from models.py
from .models import Contact, Sms, VoiceMail, User

# importing api view and status and response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# view to add contact. using user id to add contact. user is as request.data.get("userid"). use functional based view. contact information contact_name, contact_email, contact_telephonenumber is as request.data.get("contact_name"), request.data.get("contact_email"), request.data.get("contact_telephonenumber")
@api_view(['POST'])
def add_contact(request):
    if request.method == 'POST':
        user = request.data.get("userid")
        contact_name = request.data.get("contact_name")
        contact_email = request.data.get("contact_email")
        contact_telephonenumber = request.data.get("contact_phone_number")
        # if contact_name, contact_email, contact_telephonenumber is not empty then add contact
        if contact_name and contact_email and contact_telephonenumber:
            # get user from User model
            user = User.objects.get(id=user)
            # create contact using Contact model
            contact = Contact.objects.create(user=user, contact_name=contact_name, contact_email=contact_email, contact_phone_number=contact_telephonenumber)
            # save contact
            contact.save()
            # return response as contact added successfully
            return Response({"message": "Contact added successfully"}, status=status.HTTP_201_CREATED)
        # else return response as contact not added
        else:
            return Response({"message": "Contact not added"}, status=status.HTTP_400_BAD_REQUEST)
        
# view to get contact. using user id to get contacts. user is as request.query_params.get("userid"). use functional based view.
@api_view(['GET'])
def get_contacts(request):
    if request.method == 'GET':
        user = request.query_params.get("userid")
        # if user is not empty then get contact
        if user:
            # get user from User model
            user = User.objects.get(id=user)
            # get contacts using Contact model
            contacts = Contact.objects.filter(user=user)
            # serialize contacts using ContactSerializer
            serializer = ContactSerializer(contacts, many=True)
            # return response as contacts
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no contacts found
        else:
            return Response({"message": "No contacts found"}, status=status.HTTP_400_BAD_REQUEST)