# importing contactSerializer, smsSerializer, voiceMailSerializer, userSerializer from serializers.py
from .serializers import ContactSerializer, SmsSerializer, VoiceMailSerializer
# importing Contact, Sms, VoiceMail, User from models.py
from .models import Contact, Sms, VoiceMail, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# importing api view and status and response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# importing Q for for search 
from django.db.models import Q
from django.contrib.auth.models import User
# make_password for password encryption
from django.contrib.auth.hashers import make_password

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
        
        
# view to delete contact. using contact id to delete contact. contact is as request.data.get("contactid"). use functional based view.
@api_view(['DELETE'])
def delete_contact(request):
    if request.method == 'DELETE':
        contact = request.data.get("contactid")
        # if contact is not empty then delete contact
        if contact:
            # get contact from Contact model
            contact = Contact.objects.get(id=contact)
            # delete contact
            contact.delete()
            # return response as contact deleted successfully
            return Response({"message": "Contact deleted successfully"}, status=status.HTTP_200_OK)
        # else return response as contact not deleted
        else:
            return Response({"message": "Contact not deleted"}, status=status.HTTP_400_BAD_REQUEST)
        
# view to update contact. using contact id to update contact. contact is as request.data.get("contactid"). use functional based view. contact information contact_name, contact_email, contact_telephonenumber is as request.data.get("contact_name"), request.data.get("contact_email"), request.data.get("contact_telephonenumber")
@api_view(['PUT'])
def update_contact(request):
    if request.method == 'PUT':
        contact = request.data.get("contactid")
        contact_name = request.data.get("contact_name")
        contact_email = request.data.get("contact_email")
        contact_telephonenumber = request.data.get("contact_phone_number")
        # if contact is not empty then update contact
        if contact:
            # get contact from Contact model
            contact = Contact.objects.get(id=contact)
            # if contact_name is not empty then update contact_name
            if contact_name:
                contact.contact_name = contact_name
            # if contact_email is not empty then update contact_email
            if contact_email:
                contact.contact_email = contact_email
            # if contact_telephonenumber is not empty then update contact_telephonenumber
            if contact_telephonenumber:
                contact.contact_phone_number = contact_telephonenumber
            # save contact
            contact.save()
            # return response as contact updated successfully
            return Response({"message": "Contact updated successfully"}, status=status.HTTP_200_OK)
        # else return response as contact not updated
        else:
            return Response({"message": "Contact not updated"}, status=status.HTTP_400_BAD_REQUEST)
#  view to search for contact_name, contact_email, contact_telephonenumber. using user id to search contact. user is as request.query_params.get("userid"). use functional based view. search is as request.query_params.get("search")
@api_view(['GET'])
def search_contact(request):
    if request.method == 'GET':
        user = request.query_params.get("userid")
        search = request.query_params.get("search")
        # if user is not empty then search contact
        if user:
            # get user from User model
            user = User.objects.get(id=user)
            # search contact using Contact model
            contacts = Contact.objects.filter(Q(contact_name__icontains=search) | Q(contact_email__icontains=search) | Q(contact_phone_number__icontains=search), user=user)
            # serialize contacts using ContactSerializer
            serializer = ContactSerializer(contacts, many=True)
            # return response as contacts
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no contacts found
        else:
            return Response({"message": "No contacts found"}, status=status.HTTP_400_BAD_REQUEST)
        
        


#user specific views


@api_view(['POST'])
def change_email(request):
    user_id = request.data.get("user_id")
    email = request.data.get("email")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.email = email
        user.save()
        return Response({"message": "Email changed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def change_password(request):
    user_id = request.data.get("user_id")
    password = request.data.get("password")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def change_username(request):
    user_id = request.data.get("user_id")
    username = request.data.get("username")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.username = username
        user.save()
        return Response({"message": "Username changed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(["POST"])
def create_account(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    # check whether user exists or not
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        User.objects.create(username=username, password=make_password(password), email=email)
#        user.save()
        return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)
    
# delete account
@api_view(["DELETE"])
def delete_account(request):
    user_id = request.data.get("user_id")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({"message": "Account deleted successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    

class MyTokenObtainPair(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # serializer = UserSerializerWithToken(self.user).data
        # for k,v in serializer.items():
        # data[k] = v
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPair

